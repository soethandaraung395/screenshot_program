/*import 'package:flutter/material.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      title: 'Exercise 5',
      home: TodoListScreen(),
    );
  }
}

class TodoListScreen extends StatefulWidget {
  @override
  _TodoListScreenState createState() => _TodoListScreenState();
}

class _TodoListScreenState extends State<TodoListScreen> {
  final List<String> _toDoItems = [];
  
  void _addToDoItem(String task) {
      if (task.isNotEmpty) {
        setState(() {
          _toDoItems.add(task);
        });
      }
    }

  void _add() {
    showDialog(
      context: context,
      builder: (BuildContext context) {
        String newTask = '';
        return AlertDialog(
          title: const Text('Add a new To-Do'),
          content: const TextField(

            decoration: const InputDecoration(
              hintText: 'Enter your task here',
            ),
          ),
          actions: <Widget>[
            ElevatedButton(
              child: const Text('Add'),
              onPressed: () {
                _addToDoItem(newTask);
                Navigator.of(context).pop();
              },
            ),
          ],
        );
      },
    );
  }


  @override
  Widget build(BuildContext context) {
    return Container(
      decoration: BoxDecoration(
        border: Border.all(
          color: Colors.black,
          width: 10.0,
        ),
      ),
      child: Scaffold(
        appBar: AppBar(
          title: Text("To-Do List"),
          backgroundColor: Colors.blue,
        body: ListView.builder(
          itemCount: _toDoItems.length,
          itemBuilder: (BuildContext context, int index) {
            return ListTile(
              title: Text(_toDoItems[index]),
            );
          },
        ),
        ),



      floatingActionButton: FloatingActionButton(
        onPressed: _add,
        tooltip: 'add',
        child: Icon(Icons.add, color: Colors.blue),
      ),

      ),
    );
  }
}*/

import 'package:flutter/material.dart';

void main() => runApp(const MyApp());

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'To-Do List',
      home: const ToDoListScreen(),
    );
  }
}

class ToDoListScreen extends StatefulWidget {
  const ToDoListScreen({super.key});

  @override
  _ToDoListScreenState createState() => _ToDoListScreenState();
}

class _ToDoListScreenState extends State<ToDoListScreen> {
  final List<String> _toDoItems = [];

  void _addToDoItem(String task) {
    if (task.isNotEmpty) {
      setState(() {
        _toDoItems.add(task);
      });
    }
  }

  void _promptAddToDoItem() {
    showDialog(
      context: context,
      builder: (BuildContext context) {
        String newTask = '';
        return AlertDialog(
          title: const Text('New To-Do'),
          content: TextField(
            onChanged: (value) {
              newTask = value;
            },
            decoration: const InputDecoration(
              hintText: 'Enter your task here',
            ),
          ),
          actions: <Widget>[
            TextButton(
              child: const Text('Cancel'),
              onPressed: () {
                Navigator.of(context).pop();
              },
            ),
            TextButton(
              child: const Text('Add'),
              onPressed: () {
                _addToDoItem(newTask);
                Navigator.of(context).pop();
              },
            ),
          ],
        );
      },
    );
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('To-Do List'),
        backgroundColor: Colors.blue,
      ),
      body: ListView.builder(
        itemCount: _toDoItems.length,
        itemBuilder: (BuildContext context, int index) {
          return ListTile(
            title: Text(_toDoItems[index]),
            tileColor: Colors.red,
          );
        },
      ),
      floatingActionButton: FloatingActionButton(
        onPressed: _promptAddToDoItem,
        backgroundColor: Colors.blue,  // FloatingActionButtonの色を青色に設定
        child: const Icon(Icons.add),
      ),
    );
  }
}
