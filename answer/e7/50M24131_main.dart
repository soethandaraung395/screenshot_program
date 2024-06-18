import 'package:flutter/material.dart';

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
  final List<String> _todoList = [];

  void _addTodoItem(String task) {
    if (task.isNotEmpty) {
      setState(() {
        _todoList.add(task);
      });
    }
  }

  void _showAddTodoDialog() {
    String newTodo = '';

    showDialog(
      context: context,
      builder: (BuildContext context) {
        return AlertDialog(
          title: Text('Add a new To-Do'),
          content: TextField(
            onChanged: (value) {
              newTodo = value;
            },
            decoration: InputDecoration(
              labelText: 'Enter your task',
            ),
          ),
          actions: <Widget>[
            ElevatedButton(
              onPressed: () {
                _addTodoItem(newTodo);
                Navigator.of(context).pop();
              },
              child: Text('Add'),
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
          title: Center(
            child: Text("To-Do List"),
          ),
          backgroundColor: Colors.blue,
        ),
        body: _todoList.isEmpty
            ? Center(
                child: Text(
                  '',
                ),
              )
            : ListView.builder(
                itemCount: _todoList.length,
                itemBuilder: (context, index) {
                  return ListTile(
                    title: Text(
                      _todoList[index],
                      style: TextStyle(fontSize: 18),
                    ),
                    tileColor: Colors.red,
                    contentPadding: EdgeInsets.symmetric(horizontal: 16.0),
                  );
                },
              ),
        floatingActionButton: FloatingActionButton(
          onPressed: _showAddTodoDialog,
          tooltip: 'Add',
          child: Icon(Icons.add),
          backgroundColor: Colors.blue,
        ),
      ),
    );
  }
}
