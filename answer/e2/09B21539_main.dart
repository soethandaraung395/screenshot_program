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
            reverse: true, // リストを逆順に表示
            shrinkWrap: true, // リストを親コンテナの高さに合わせる
            physics: const ClampingScrollPhysics(), // スクロールの挙動を修正
            itemCount: 5,
            itemBuilder: (BuildContext context, int index) {
              return ListTile(
                title: Text('Item $index'),
                subtitle: Text('This is the subtitle for item $index'),
                leading: CircleAvatar(
                  child: Text('$index'),
                ),
                trailing: const Icon(Icons.arrow_back),
                onTap: () {
                  print('Tapped item $index');
                },
              );
            },
          ),
        ),
      ),
    );
  }
}
