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
  List<String> items = []; //todo list 初期状態はvoid
  final TextEditingController _textFieldController =
      TextEditingController(); //ダイアログに入力された文字列を記憶
  void _addItem(String item) {
    setState(() {
      items.add(item);
    }); //リストに追加する
    _textFieldController.clear();
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
        body: Center(
            //中央配置要素
            child: ListView.builder(
          //リストを表示
          itemCount: items.length,
          itemBuilder: (context, index) {
            return ListTile(
              title: Text(
                items[index],
                style: TextStyle(fontSize: 18),
              ),
              tileColor: Colors.red,
            );
          },
        )),
        floatingActionButton: FloatingActionButton(
          //フローティングんボタン
          onPressed: () {
            showDialog(
              context: context,
              barrierDismissible: false,
              builder: (context) {
                return AlertDialog(
                  title: Text('Add a new to-do'),
                  content: TextField(
                    controller: _textFieldController,
                  ),
                  actions: [
                    //addボタン
                    ElevatedButton(
                      child: Text("Add"),
                      onPressed: () {
                        if (_textFieldController.text.isNotEmpty) {
                          _addItem(_textFieldController.text); //addが押されたらリストに追加
                          Navigator.pop(context);
                        }
                      },
                    ),
                  ],
                );
              },
            );
          },
          backgroundColor: Colors.blue,
          child: const Icon(Icons.add),
        ),
      ),
    );
  }
}
