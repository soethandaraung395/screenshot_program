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
  final TextEditingController _textEditingController = TextEditingController();

  void _showAddTodoDialog() {
    showDialog(
      context: context,
      builder: (BuildContext context) {
        return AlertDialog(
          title: const Text('Add a new To-Do'),
          content: TextField(
            controller: _textEditingController,
            decoration: const InputDecoration(
              hintText: 'Enter your to-do',
            ),
          ),
          actions: <Widget>[
            ElevatedButton(
              onPressed: () {
                setState(() {
                  if (_textEditingController.text.isNotEmpty) {
                    _todoList.add(_textEditingController.text);
                  }
                });
                Navigator.of(context).pop();
                _textEditingController.clear();
              },
              child: const Text('追加'),
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
          title: const Text("To-Do List"),
          backgroundColor: Colors.blue,
        ),
        body: Container(

          child: ListView.builder(
            itemCount: _todoList.length,
            itemBuilder: (context, index) {
              return ListTile(
                title: Text(
                  _todoList[index],
                  style: TextStyle(
                    color: Colors.black, // タイトルの色を赤に設定
                    fontSize: 18, // フォントサイズを18に設定
                  ),
                ),
                tileColor: Colors.red,
              );
            },
          ),
        ),
        floatingActionButton: FloatingActionButton(
          onPressed: _showAddTodoDialog, // ボタンが押されたときにダイアログを表示
          child: const Icon(Icons.add), // "add" アイコンを使用
          backgroundColor: Colors.blue, // ボタンの色を青に設定
        ),
      ),
    );
  }
}
