import 'package:flutter/material.dart';

void main() => runApp(const MyApp());

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    final List<int> data = List<int>.generate(5, (int index) => index).reversed.toList();

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
            itemCount: data.length,
            itemBuilder: (BuildContext context, int index) {
              final int item = data[index];
              return ListTile(
                title: Text('Item $item'),
                subtitle: Text('This is the subtitle for item $item'),
                leading: CircleAvatar(
                  child: Text('$item'),
                ),
                trailing: const Icon(Icons.arrow_back),
                onTap: () {
                  print('Tapped item $item');
                },
              );
            },
          ),
        ),
      ),
    );
  }
}
