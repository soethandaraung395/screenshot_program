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
  List<String> tasks = []; // リストを格納するためのリスト

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
          itemCount: tasks.length,
          itemBuilder: (BuildContext context, int index) {
            return ListTile(
              title: Text(tasks[index],
              style: TextStyle(color: Colors.black, fontSize: 18,),
              ), 
              tileColor: Colors.red,
            );
          },
        ),
        floatingActionButton: FloatingActionButton(
          onPressed: () {
            String title = "";
            showDialog(
              context: context,
              builder: (BuildContext context) {
                return AlertDialog(
                  title: Text("Add a new To-Do"),
                  content: TextField(
                    onChanged: (textField) {
                      // タイトルを更新する処理
                      // (ここではタイトルの更新のみ行い、実際のリストへの追加はElevatedButton内で行う)
                      // setState()を使って再描画を行う
                      setState(() {
                        // タイトルを更新
                        title = textField;
                      });
                    },
                  ),
                  actions: [
                    ElevatedButton(
                      child: Text("Add"),
                      onPressed: () {
                        // 新しいタスクをリストに追加する処理
                        setState(() {
                          tasks.add(title); // タイトルをリストに追加
                        });
                        Navigator.of(context).pop(); // ダイアログを閉じる
                      },
                    ),
                  ],
                );
              },
            );
          },
          tooltip: 'Add Task',
          child: Icon(Icons.add),
          backgroundColor: Colors.blue,
        ),
      ),
    );
  }
}
