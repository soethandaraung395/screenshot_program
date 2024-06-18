import 'package:flutter/material.dart';

void main() => runApp(const MyApp());

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      title: 'ListView Example',
      home: Container(
        decoration: BoxDecoration(
          border: Border.all(
            color: Colors.black,
            width: 10.0,
          ),
        ),
        child: Scaffold(
          appBar: AppBar(
            title: const Text('ListView Example'),
          ),
          body: ListView.builder(
            itemCount: 5,
            itemBuilder: (BuildContext context, int index) {
              int rev_index = 4 - index;
              return ListTile(
                title: Text('Item $rev_index'),
                subtitle: Text('This is the subtitle for item $rev_index'),
                leading: CircleAvatar(
                  child: Text('$rev_index'),
                ),
                trailing: const Icon(Icons.arrow_back),
                onTap: () {
                  print('Tapped item $rev_index');
                },
              );
            },
          ),
        ),
      ),
    );
  }
}
