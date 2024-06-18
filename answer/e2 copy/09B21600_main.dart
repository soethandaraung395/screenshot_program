import 'package:flutter/material.dart';

void main() => runApp(const MyApp());

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'ListView Example',
      home: Scaffold(
        appBar: AppBar(
          title: const Text('ListView Example'),
        ),
        body: ListView.builder(
          itemCount: 5,
          itemBuilder: (BuildContext context, int index) {
            int reversedIndex = 4 - index;
            return ListTile(
              title: Text('Item $reversedIndex'),
              subtitle: Text('This is the subtitle for item $reversedIndex'),
              leading: CircleAvatar(
                child: Text('$reversedIndex'),
              ),
              trailing: const Icon(Icons.arrow_back),
              onTap: () {
                print('Tapped item $reversedIndex');
              },
            );
          },
        ),
      ),
    );
  }
}
