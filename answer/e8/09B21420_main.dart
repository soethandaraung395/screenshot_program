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
 List<String> _todoItems = []; // 追加: ToDoアイテムのリスト

  void _addTodoItem(String todoItem) {
    setState(() {
      _todoItems.add(todoItem);
    });
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
        body: ListView.builder( // 追加: ToDoアイテムのリスト表示
          itemCount: _todoItems.length,
          itemBuilder: (context, index) {
            return ListTile(
              title: Text(
                _todoItems[index],
                style: TextStyle(fontSize: 18.0),
              ),
              tileColor: Colors.red, // 追加: タイルの色を赤に
            );
          },
        ),
        floatingActionButton: FloatingActionButton( // 追加: フローティングアクションボタン
          onPressed: () {
            showDialog(
              context: context,
              builder: (context) {
                String newTodo = ''; // テキストフィールドの値を保持する変数
                return AlertDialog(
                  title: Text('Add a new To-Do'), // 追加: ダイアログのタイトル
                  content: TextField( // 追加: テキストフィールド
                    onChanged: (value) {
                      newTodo = value; // 入力値をnewTodoに代入
                    },
                     decoration: InputDecoration(
                      hintText: 'Enter your To-Do',
                    ),
                  ),
                  actions: <Widget>[
                    ElevatedButton( // 追加: 昇格ボタン
                      onPressed: () {
                        if (newTodo.isNotEmpty) { // 入力が空でない場合にのみ追加
                          _addTodoItem(newTodo); // リストに追加
                          Navigator.of(context).pop(); // ダイアログを閉じる
                        }
                      },
                      child: Text('Add'), // ボタンのテキスト
                    ),
                  ],
                );
              },
            );
          },
          tooltip: 'Add Todo', // ツールチップ
          child: Icon(Icons.add), // アイコン
          backgroundColor: Colors.blue, // ボタンの背景色を青に
        ),
      ),
    );
  }
}
