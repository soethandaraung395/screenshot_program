import 'package:flutter/material.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return const MaterialApp(
      debugShowCheckedModeBanner: false,
      home: MyHomePage(),
    );
  }
}

class MyHomePage extends StatefulWidget {
  const MyHomePage({super.key});

  @override
  _MyHomePageState createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {
  void _showAlertDialog() {
    showDialog(
      context: context,
      builder: (BuildContext context) {
        return AlertDialog(
          title: const Text('Result file'),
          content: const Text('Oops! Your proposal is accepted.'),
          actions: <Widget>[
            TextButton(
              child: const Text('Enough'),
              onPressed: () {
                Navigator.of(context).pop();
              },
            ),
            ElevatedButton(
              child: const Text('Continue'),
              onPressed: () {
                Navigator.of(context).pop();
              },
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
          title: const Text('AlertDialog Example'),
        ),
        body: Center(
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              const Text('Hello, Guys!'),
              const SizedBox(height: 20),
              const Icon(Icons.favorite, size: 48, color: Colors.red),
              const SizedBox(height: 20),
              OutlinedButton(
                onPressed: _showAlertDialog,
                child: const Text('Press me'),
              ),
            ],
          ),
        ),
      ),
    );
  }
}
