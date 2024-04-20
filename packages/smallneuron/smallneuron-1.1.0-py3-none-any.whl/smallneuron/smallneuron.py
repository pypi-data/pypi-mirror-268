from time import sleep
import threading
import queue
import re
import os
import json
from .logger import Logger
import traceback
from datetime import datetime

#
# Para que funcione el tooltip debe set en formato svg, para generarlo usar:
#
#    dot -Tsvg -osmallneuron.svg smallneuron.dot
#
# Despues visualizar smallneuron.svg con chrome
#

log= Logger("smallneuron")

# tooltip format
def ttfmt(txt):
    # Eliminamos los espacion entre \n y el primer caracter
    return re.sub(r"\n +", "\n", txt)


class Node:
    nodelist = {}

    def __init__(self, state, desc="", style=""):
        self.state = state
        self.event_manager = None  # Este link es llenado durante addEdge del event manager
        self.desc = desc
        self.style = style
        self._cmd=False
        if state in Node.nodelist:
            raise "Estado ya existe como Nodo" + state
        Node.nodelist[state] = self

    def enter(self, event, args, stateFrom):
        pass #  print("Node: Enter:", self.state, "event trigger:", event, "from", stateFrom)

    def leave(self, event, args, stateTo):
        pass # print("Node: Leave:", self.state, "event trigger:", event, "to", stateTo)

    def __eq__(self, other):
        return self.state == other.state


class LambdaNode(Node):
    def __init__(self, state, lambdaEnter, desc="", style=""):
        super().__init__(state, desc, style)
        self.enter = lambdaEnter

    def __eq__(self, other):
        return self.state == other.state


# def TimerThread(queue, event, args, time, logging):
#     # print("TimerThread ", event, time, "s")
#     sleep(time)
#     queue.put((event, args, { "time": time, "logging":logging}))
#     # print("TimerThread ", event, " done")


class EventManager:
    def __init__(self, graphDir_and_prefix="."):
        self.currentState = None
        self.currentArgs = None
        self.currentNode =None
        self.prevState = None
        self.count = 0 # state count
        self.graph_n = 0
        self.events = queue.SimpleQueue()
        self.net = (
            {}
        )  # estructura es { "evento1": { "estado Origen1" : (nodoDestino1, "event_desc1" ), "estadoOrigen2": (nodoDestino2, "event_desc2") }, "evento2"...
        self.cmds = (
            {}
        )  # estructura es { "evento1": (nodoDestino1, "event_desc1" ), "evento2": (nodoDestino2, "event_desc2")...
        self.graphDir=graphDir_and_prefix

        log.notice("*** STARTED ***")

    def putEvent(self, event, params=None):  # lanzamos un evento ahora
        #print("pushEvent:", event, "params:", params) 
        if params == None:
            params = {}

        self.events.put((event, params, {}))

    def watchEvent(self,event, event_args={}, event_pattern=None, 
                bridge=None, bridge_args={}, mode="loop",period=1):
                watcher=SnWatcher(self,event,event_args, event_pattern)
                watcher.run(bridge,bridge_args,mode,period)
                return watcher


    def linkEdge(self, event, nodeFrom: Node, nodeTo: Node, desc=""):
        if event in self.cmds:
            print("Error event already in cmds ", event)
            raise "Error event already in cmds"
        elif event in self.net:
            if nodeFrom.state in self.net[event]:
                print("Error edge already included ", event, nodeFrom, nodeTo)
                raise "Error edge already included"
            else:
                self.net[event][nodeFrom.state] = (nodeTo, desc)
        else:
            self.net[event] = {nodeFrom.state: (nodeTo, desc)}
            nodeFrom.event_manager = self
            nodeTo.event_manager = self

    def linkCmd(self, event, nodeTo: Node, desc=""):
        if event in self.cmds:
            print("Error event already in cmds ", event)
            raise "Error event already in cmds "
        elif event in self.net:
            print("Error event already in edges ", event)
            raise "Error event already in edges "
        else:
            self.cmds[event] = (nodeTo, desc)
            nodeTo.event_manager = self
            nodeTo._cmd =True

    def graph(self, f, bold_event=None):
        f.write("digraph { \n")
        f.write('  layout="dot" \n')
        f.write("  //rankdir=LR \n")
        f.write('  graph [ overlap="true" fontsize = 10 ] \n')
        f.write('  node [ style="rounded,filled" shape="rect" fillcolor="#0000a0", fontcolor=white ]')
        # print("write ", len(Node.nodelist), "nodes")
        for state in Node.nodelist:
            node = Node.nodelist[state]
            style = node.style
            if node.desc != "":
                style = style + ' tooltip="' + ttfmt(node.desc) + '"'
            if state == self.currentState:
                style = style + ' fillcolor="#a00000"'
            elif state == self.prevState:
                style = style + ' fillcolor="#fed104" fontcolor=black'
            if node._cmd == True:
                style = style + ' fillcolor="#a0a0a0"'

            f.write("%s [%s]\n" % (state, style))

        # print("write ", len(self.net), "events")
        for event in self.net:
            for state_from in self.net[event]:
                state_to = self.net[event][state_from][0].state
                desc = self.net[event][state_from][1]

                tooltip = ""
                if desc != "":
                    tooltip = 'labeltooltip="' + ttfmt(desc) + '" tooltip="' + ttfmt(desc) + '"'

                if bold_event == event and state_from == self.prevState and state_to == self.currentState:
                    args = " " + json.dumps(self.currentArgs).replace('"', '\\"')
                    f.write(
                        '%s -> %s [ label = "%s" fontcolor="red" %s ]\n'
                        % (state_from, state_to, event + args, tooltip)
                    )
                else:
                    f.write('%s -> %s [ label = "%s" %s  ]\n' % (state_from, state_to, event, tooltip))

        # print("write ", len(self.cmds), "commands")
        if len(self.cmds) > 0:
            f.write(
                '"*" [ label="" style="filled" fixedsize=true width=0.2 shape="circle" fillcolor="red" tooltip = "desde todos los estados" ]\n'
            )
            for event in self.cmds:
                state_to = self.cmds[event][0].state
                desc = self.cmds[event][1]

                tooltip = ""
                if desc != "":
                    tooltip = 'labeltooltip="' + ttfmt(desc) + '" tooltip="' + ttfmt(desc) + '"'

                if bold_event == event:
                    f.write('"*" -> %s [ label = "%s" fontcolor="red" %s ]\n' % (state_to, event, tooltip))
                else:
                    f.write('"*" -> %s [ label = "%s" %s ]\n' % (state_to, event, tooltip))

        f.write("}\n")
            
    def printGraph(self,bold_event=None):
        # Si ya hay archivo base lo renombramos al nombre historico
        filename = self.graphDir+"_"+datetime.now().strftime("%Y-%m-%d_%H:%M:%S_") + \
            str(self.count%10000).zfill(4)+"_"+str(self.graph_n%10000).zfill(4)+".dot"
        log.info("dotFile:",filename)
        self.graph_n=self.graph_n+1
        # Creamos el archivo con todos los permisos
        # The default umask is 0o22 which turns off write permission of group and others
        os.umask(0)

        desc = os.open(
            path=filename,
            flags=(
                os.O_WRONLY  # access mode: write only
                | os.O_CREAT  # create if not exists
                | os.O_TRUNC  # truncate the file to zero
            ),
            mode=0o666
        )

        with open(desc, 'w') as f:
            self.graph(f, bold_event)
    
    def start(self, n_first: Node):
        n_start = Node(
            "_start_",
            desc="start",
            style='label="" style="filled" fixedsize=true width=0.2 shape="circle" fillcolor="green"',
        )
        self.linkEdge("_start_", n_start, n_first, desc="start")
        self.currentState = "_start_"
        self.currentNode=n_start
        threading.Thread(target=self.loop).start()
        self.putEvent("_start_")  # lanzamos evento de inicio

    def loop(self):
        try:
            self.printGraph()
            while True:
                log.notice("[",self.count,"] State:", self.currentState)
                eventTuple = self.events.get()
                event  = eventTuple[0]  # text del evento
                params = eventTuple[1]  # argumentos del evento

                log.notice("[",self.count,"] Event:", event, params)
                

                # eliminamos el validUntil, para que no quede en un loop
                validUntil=self.count
                if type(params) == dict:
                    validUntil=params.pop("validUntil", self.count)

                if validUntil < self.count:
                    log.warn("[",self.count,"] ", event, " is caduced ", validUntil, "<", self.count)

                elif event in self.net:
                    if not self.currentState in self.net[event]:
                        log.warn("[",self.count,"] ", event, " not valid for state ", self.currentState, "discarted!")
                    else:
                        node: Node = self.net[event][self.currentState][0]
                        log.info("[",self.count,"] entqer ", node.state, params, self.currentState)
                        
                        # indicamos al nodo actual que salimos
                        self.currentNode.leave(event,params,node.state)
                        
                        # Entramos al nodo nuevo
                        node.enter(event, params, self.currentState)
                        self.currentNode=node
                        self.prevState = self.currentState
                        self.currentState = node.state
                        self.currentArgs = params
                        self.count = self.count + 1  # increment event count
                        self.printGraph(event)
                elif event in self.cmds:
                    log.info("[", self.count, "] Manager new  cmd ", event)
                    node: Node = self.cmds[event][0]
                    node.enter(event, params, self.currentState)
                    self.printGraph(event)
                else:
                    log.warn("[",self.count,"] ", event, " not exist")
        except Exception as e:
            log.error(e)
            log.error(traceback.format_exc())
            exit(1)


class SnWatcher():
    '''
    Cada instancia de esta clase monitorea la funcion check() del bridge, con bridge_args como parametros,
    Si la respuesta contiene el bridge_pattern se dispara el evento con event_args que se le agrega "data": respuesta

    Consideraciones importantes de la funcion check:
        1. Debe recibir como parametros los mismo elementos del dict bridge_args de enter()
        2. Debe retornar un diccionario con almenos el elemento data, todo el diccionario retornado
           seran parte del argumento del evento junto a los event_args
        3. Si se repiten los elementos retornados por check() con los events_args mandan los de check()
    una respuesta  hasta que  respuesta, bloqueando
    '''
    def __init__(self, eventManager, event, event_args={}, event_pattern=None):
        self.em=eventManager
        self.event=event
        self.event_args=event_args
        self.event_pattern=event_pattern
        self.stoploop=False
        self.thread=None
        log.debug("SnWatcher created")

    def run(self, bridge, bridge_args={}, mode="loop",period=1):
        '''
        modos validos:
            loop: (default) Se leera permanentenemente hasta el stop, genenrando multiples eventos
            match: Se iterara hasta el primer match, genera 1 evento
            noloop: Termina despues de la primera llamada, puede no generar evento alguno
        '''
        log.debug("SnWatcher.run")
        if self.thread == None:
            self.stoploop=False
            try:
                log.debug("SnWatcher.run Thread create")
                self.thread=threading.Thread(target=SnWatcher._check, args=(self,[bridge,bridge_args,mode, period]))
                log.debug("SnWatcher.run Thread to start")
                self.thread.start()
                log.debug("SnWatcher.run Thread to started")
            except Exception as e:
                log.error(e)
                log.error(traceback.format_exc())
               
            log.debug("SnWatcher.run done")
            return True
        log.debug("SnWatcher.run fail")
        return False

    def _check(self, args):
        log.debug("SnWatcher._check loop start",args)
        try:
            [bridge,args,mode, period] = args
            while not self.stoploop:
                resp=bridge.check(**args)

                # Si la respuesta no es un dict
                # creamos uno con la respuesta como data
                if type(resp) != dict:
                    data=resp
                    resp={"data":data}

                if self.event_pattern == None or re.search(self.event_pattern, resp["data"]) != None:
                    self.em.putEvent(self.event, dict(self.event_args,**resp))
                    log.info("SnWatcher trigger", self.event_args)
                    if mode=="match":
                        log.debug("SnWatcher._check loop exit, match")
                        return

                if mode=="noloop" :
                    log.debug("SnWatcher._check loop exit, noloop")
                    return
                    
                # default mode is loop 
                sleep(period)
            log.debug("SnWatcher._check loop exit, stop")
        except Exception as e:
            log.error(e)
            log.error(traceback.format_exc())

    def stop(self):
        self.stoploop=True
        self.thread.join()
        self.thread=None