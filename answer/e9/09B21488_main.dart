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

  void _addTodoItem(String todo) {
    setState(() {
      _todoList.add(todo);
    });
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
          ),
          actions: [
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
          title: Text("To-Do List"),
          backgroundColor: Colors.blue,
        ),
        body: ListView.builder(
          itemCount: _todoList.length,
          itemBuilder: (context, index) {
            return ListTile(
              title: Text(
                _todoList[index],
                style: TextStyle(fontSize: 18),
              ),
              tileColor: Colors.red,
            );
          },
        ),
        floatingActionButton: FloatingActionButton(
          onPressed: _showAddTodoDialog,
          backgroundColor: Colors.blue,
          child: Icon(Icons.add),
        ),
      ),
    );
  }
}
