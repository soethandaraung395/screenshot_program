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

  final TextEditingController _textFieldController = TextEditingController();
  List<String> _titles = [];

  void _addTitleToList() {
    setState(() {
      final enteredText = _textFieldController.text;
      if (enteredText.isNotEmpty) {
        _titles.add(enteredText);
        _textFieldController.clear();
      }

            


          //     Expanded(
          //       child: ListView.builder(
          //         itemCount: _titles.length,
          //         itemBuilder: (context, index) {
          //           return ListTile(
          //             title: Text(_titles[index]),
          //             );
          //     },
          //   ),
          // ),
    });
  }

    Future<void> _showMyDialog(BuildContext context) async {
    return showDialog<void>(
      context: context,
      builder: (BuildContext context) {
        return AlertDialog(
          title: Text('Add a new To-Do'),
          content: Column(
            mainAxisSize: MainAxisSize.min,
            children: <Widget>[
              TextField(
                controller: _textFieldController,
                decoration: InputDecoration(
                  hintText: 'Enter your task',
                ),
              ),
              SizedBox(height: 16),
              ElevatedButton(
                onPressed: () {
                  _addTitleToList();
                  Navigator.of(context).pop(); // Close the dialog
                },
                child: Text('Add'),
                
              ),
      
            ],
          ),
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

        body: Center(
          child: ListView.builder(
                  itemCount: _titles.length,
                  itemBuilder: (context, index) {
                    return ListTile(
                      title: Text(_titles[index]),
                      tileColor: Colors.red,
                      );
              },
            ),
          
        ),
        floatingActionButtonLocation: FloatingActionButtonLocation.endFloat,
        floatingActionButton: FloatingActionButton(
          onPressed: () {
            _showMyDialog(context);
          },
          child: Icon(Icons.add),
          backgroundColor: Colors.blue,
          ),
        












      ),
    );
  }
}
