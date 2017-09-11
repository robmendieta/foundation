# Basic ROS commands

## roscore
Creates a ROS Master
```
$ roscore
```

## rostopic 
* list: show published topics.
```
$ rostopic list
```
* info: shows the message type, publishers and subscribers of a topic.
```
$ rostopic type <topic>
```
* echo: subscribe to a topic, prints published message.
```
$ rostopic echo <topic>
```
* pub: creates a temporary node publishing to a topic.
```
$ rostopic pub <topic> <message_type> <message>
```

## rosnode
* list: show all nodes.
```
$ rosnode list
```
* info: shows info (subscriptions, publications, services) of a node.
```
$ rosnode info <node>
```
* kill: closes a node.
```
$ rosnode kill <node>
```

## rosservice
* list: show all services.
```
$ rosservice list
```
* info: show node, type, URI and arguments of service.
```
$ rosservice info <service>
```
* call: creates a temporary request to a service.
```
$ rosservice call <service> <request>
```

## rosmsg
* show: show definition of a message.
```
$ rosmsg show <message>
```

## rqt_graph
Show a graph representation of communication between nodes, topics and services.