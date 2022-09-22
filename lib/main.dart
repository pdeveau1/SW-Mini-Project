import 'package:flutter/material.dart';
import 'package:firebase_core/firebase_core.dart';
import 'firebase_options.dart';
import 'package:http/http.dart' as http;
import 'dart:async';
import 'dart:core';
import 'api.dart';
import 'package:twitter_login/twitter_login.dart';
import 'package:flutter/foundation.dart' show kIsWeb;
import 'package:platform/platform.dart';
import 'package:universal_io/io.dart';
import 'package:url_launcher/url_launcher.dart';
import 'dart:convert';
import 'package:google_sign_in/google_sign_in.dart';
// import 'package:flutter_twitter_login/flutter_twitter_login.dart';

GoogleSignIn _googleSignIn = GoogleSignIn(
  // Optional clientId
  clientId:
      '792845774494-c9j0iod7e1an4ksih13n7a8l8p1ebnhf.apps.googleusercontent.com',
  scopes: <String>[
    'email',
    'https://www.googleapis.com/auth/contacts.readonly',
  ],
);
Future<void> main() async {
  // WidgetsFlutterBinding.ensureInitialized();
  await Firebase.initializeApp(
    options: DefaultFirebaseOptions.currentPlatform,
  );
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  // This widget is the root of your application.
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Mini Test',
      theme: ThemeData(
        // This is the theme of your application.
        //
        // Try running your application with "flutter run". You'll see the
        // application has a blue toolbar. Then, without quitting the app, try
        // changing the primarySwatch below to Colors.green and then invoke
        // "hot reload" (press "r" in the console where you ran "flutter run",
        // or simply save your changes to "hot reload" in a Flutter IDE).
        // Notice that the counter didn't reset back to zero; the application
        // is not restarted.
        primarySwatch: Colors.blue,
      ),
      home: const MyHomePage(title: 'mini-project-test'),
    );
  }
}

class MyCustomForm extends StatefulWidget {
  const MyCustomForm({super.key});

  @override
  State<MyHomePage> createState() => _MyHomePageState();
}

class MyHomePage extends StatefulWidget {
  const MyHomePage({super.key, required this.title});

  // This widget is the home page of your application. It is stateful, meaning
  // that it has a State object (defined below) that contains fields that affect
  // how it looks.

  // This class is the configuration for the state. It holds the values (in this
  // case the title) provided by the parent (in this case the App widget) and
  // used by the build method of the State. Fields in a Widget subclass are
  // always marked "final".

  final String title;

  @override
  State<MyHomePage> createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {
  int _counter = 0;
  String _list = "";
  var result = "";
  String _Bot = "b";
  String _Topic = "topic";
  String _Mood = "mood";
  bool Display = false;
  final myText = TextEditingController();
  final entries = <String>['Your follows']; // Creates growable list.
  final Bots_r = <String>[''];
  final Topics_r = <String>[''];
  final Moods_r = <String>[''];
  // final List<int> colorCodes = <int>[600, 500, 100];

  @override
  void dispose() {
    // Clean up the controller when the widget is disposed.
    myText.dispose();
    super.dispose();
  }

  void _find(String name) async {
    // setState(() async {
    print("followers");
    // var name = Text(myText.text).data;
    var id = "";
    var url = 'https://api.twitter.com/2/users/by/username/$name';
    var headers = {
      "Access-Control_Allow_Origin": "*",
      'Authorization':
          'Bearer AAAAAAAAAAAAAAAAAAAAAC6jgwEAAAAAC%2FnodFEXzSrIJpq8eGW0f6pfVNs%3DgIzHoZfPTNF57vkLlxBuAoJqVVU1zpi5VmXzcuynQP18waxJtb',
      'Cookie': 'guest_id=v1%3A166326564507290747'
    };
    var request = http.Request('GET', Uri.parse(url));

    request.headers.addAll(headers);

    http.StreamedResponse response = await request.send();

    if (response.statusCode == 200) {
      // String follower = await response.stream.bytesToString();
      // print(await response.stream.bytesToString());
      result = await response.stream.bytesToString();
      // print(result);
      final data = json.decode((result));

      print(data["data"]["id"]);
      id = data["data"]["id"];
      // result = data["data"]["id"];
    } else {
      print(response.reasonPhrase);
    }

    var url_1 = 'https://api.twitter.com/2/users/$id/following';
    var headers_1 = {
      "Access-Control_Allow_Origin": "*",
      'Authorization':
          'Bearer AAAAAAAAAAAAAAAAAAAAAC6jgwEAAAAAC%2FnodFEXzSrIJpq8eGW0f6pfVNs%3DgIzHoZfPTNF57vkLlxBuAoJqVVU1zpi5VmXzcuynQP18waxJtb',
      'Cookie': 'guest_id=v1%3A166326564507290747'
    };
    var request_1 = http.Request('GET', Uri.parse(url_1));
    print("Yes?");

    request_1.headers.addAll(headers_1);

    http.StreamedResponse response_1 = await request_1.send();
    print("hello?");

    if (response_1.statusCode == 200) {
      // String follower = await response.stream.bytesToString();
      // print(await response.stream.bytesToString());
      result = await response_1.stream.bytesToString();
      print("what?");
      // print(result);
      final data = json.decode((result));
      print(data["data"][2]["name"]);
      print(data["meta"]["result_count"]);
      result = "this is for test";
      // result = data["data"]["name"];
      entries.clear();
      Bots_r.clear();
      Moods_r.clear();
      Topics_r.clear();
      int length = data["meta"]["result_count"];
      for (var i = 0; i < length; i++) {
        entries.add(data["data"][i]["username"]);
        Bots_r.add("");
        Moods_r.add("");
        Topics_r.add("");
      }
    } else {
      print(response_1.reasonPhrase);
    }

    setState(() {
      _list = result;
    });
    // });
  }

  void _check_bot(String name, int index) async {
    // setState(() async {
    print("check bot");
    // var name = Text(myText.text).data;
    var id = "";
    var url = 'http://127.0.0.1:8000/twitter/isbot/$name';
    var headers = {
      "Access-Control_Allow_Origin": "*",
    };
    var request = http.Request('GET', Uri.parse(url));

    request.headers.addAll(headers);

    http.StreamedResponse response = await request.send();

    if (response.statusCode == 200) {
      // String follower = await response.stream.bytesToString();
      // print(await response.stream.bytesToString());
      result = await response.stream.bytesToString();
      print(result);
    } else {
      print(response.reasonPhrase);
    }

    setState(() {
      if (index >= 0) {
        Bots_r[index] = result;
      } else {
        _Bot = result;
      }
    });
  }

  void _check_topic(String name, int index) async {
    // setState(() async {
    print("check topic");
    // var name = Text(myText.text).data;
    var id = "";
    var url = 'http://127.0.0.1:8000/twitter/topics/$name';
    var headers = {
      "Access-Control_Allow_Origin": "*",
    };
    var request = http.Request('GET', Uri.parse(url));

    request.headers.addAll(headers);

    http.StreamedResponse response = await request.send();

    if (response.statusCode == 200) {
      // String follower = await response.stream.bytesToString();
      // print(await response.stream.bytesToString());
      result = await response.stream.bytesToString();
      print(result);
    } else {
      print(response.reasonPhrase);
    }

    setState(() {
      if (index >= 0) {
        Topics_r[index] = result;
      } else {
        _Topic = result;
      }
    });
  }

  void _check_mood(String name, int index) async {
    // setState(() async {
    print("check mood");
    // var name = Text(myText.text).data;
    var id = "";
    var url = 'http://127.0.0.1:8000/twitter/sentiment/$name';
    var headers = {
      "Access-Control_Allow_Origin": "*",
    };
    var request = http.Request('GET', Uri.parse(url));

    request.headers.addAll(headers);

    http.StreamedResponse response = await request.send();

    if (response.statusCode == 200) {
      // String follower = await response.stream.bytesToString();
      // print(await response.stream.bytesToString());
      result = await response.stream.bytesToString();
      print(result);
    } else {
      print(response.reasonPhrase);
    }

    setState(() {
      if (index >= 0) {
        Moods_r[index] = result;
      } else {
        _Mood = result;
      }
    });
  }

  Future<void> _launchUrl(String name) async {
    // var name = Text(myText.text).data;
    Uri _url = Uri.parse('https://twitter.com/$name');
    // Uri _url = Uri.parse('https://twitter.com/i/flow/login');
    if (!await launchUrl(_url)) {
      throw 'Could not launch $_url';
    }
  }

  Future<void> _handleSignIn() async {
    try {
      await _googleSignIn.signIn();
    } catch (error) {
      print(error);
    }
  }

  @override
  Widget build(BuildContext context) {
    // This method is rerun every time setState is called, for instance as done
    // by the _incrementCounter method above.
    //
    // The Flutter framework has been optimized to make rerunning build methods
    // fast, so that you can just rebuild anything that needs updating rather
    // than having to individually change instances of widgets.
    return Scaffold(
      appBar: AppBar(
        // Here we take the value from the MyHomePage object that was created by
        // the App.build method, and use it to set our appbar title.
        title: Text(widget.title),
      ),
      body: ListView(
        // Center is a layout widget. It takes a single child and positions it
        // in the middle of the parent.
        // Column is also a layout widget. It takes a list of children and
        // arranges them vertically. By default, it sizes itself to fit its
        // children horizontally, and tries to be as tall as its parent.
        //
        // Invoke "debug painting" (press "p" in the console, choose the
        // "Toggle Debug Paint" action from the Flutter Inspector in Android
        // Studio, or the "Toggle Debug Paint" command in Visual Studio Code)
        // to see the wireframe for each widget.
        //
        // Column has various properties to control how it sizes itself and
        // how it positions its children. Here we use mainAxisAlignment to
        // center the children vertically; the main axis here is the vertical
        // axis because Columns are vertical (the cross axis would be
        // horizontal).
        padding: const EdgeInsets.all(8),
        children: <Widget>[
          // const Text(
          //   'Enter the username below',
          // ),
          Text(
            'Enter your username below\n',
            style: Theme.of(context).textTheme.bodySmall,
          ),
          TextField(
            decoration: InputDecoration(
              border: OutlineInputBorder(),
              hintText: '@',
            ),
            controller: myText,
          ),
          const Text(
            '\n',
          ),
          TextButton(
            style: ButtonStyle(
              foregroundColor: MaterialStateProperty.all<Color>(Colors.blue),
            ),
            onPressed: () => _find((myText.text)),
            child: const Text('List my follows'),
          ),
          Text(
            'Enter username you want to search below\n',
            style: Theme.of(context).textTheme.headline5,
          ),
          TextField(
            decoration: InputDecoration(
              border: OutlineInputBorder(),
              hintText: '@',
            ),
            controller: myText,
          ),
          Text(
            "",
            style: Theme.of(context).textTheme.headline5,
          ),
          Row(
            children: [
              TextButton(
                style: ButtonStyle(
                  foregroundColor:
                      MaterialStateProperty.all<Color>(Colors.blue),
                ),
                onPressed: () => _check_bot(myText.text, -1),
                child: const Text('check Bot'),
              ),
              Text(
                _Bot,
                style: Theme.of(context).textTheme.bodyText1,
              ),
            ],
          ),
          Row(children: [
            TextButton(
              style: ButtonStyle(
                foregroundColor: MaterialStateProperty.all<Color>(Colors.blue),
              ),
              onPressed: () => _check_topic(myText.text, -1),
              child: const Text('see topic'),
            ),
            Text(
              _Topic,
              style: Theme.of(context).textTheme.bodyText1,
            ),
          ]),

          Row(children: [
            TextButton(
              style: ButtonStyle(
                foregroundColor: MaterialStateProperty.all<Color>(Colors.blue),
              ),
              onPressed: () => _check_mood(myText.text, -1),
              child: const Text('see mood'),
            ),
            Text(
              _Mood,
              style: Theme.of(context).textTheme.bodyText1,
            ),
          ]),
          Row(children: [
            TextButton(
              style: ButtonStyle(
                foregroundColor: MaterialStateProperty.all<Color>(Colors.blue),
              ),
              onPressed: () => _launchUrl(myText.text),
              child: const Text('see tweets'),
            ),
          ]),

          Text(
            '\nPofolio of my follow',
            style: Theme.of(context).textTheme.headline5,
          ),
          Container(
            height: 200,
            color: Color.fromARGB(255, 13, 235, 243),
            child: ListView.builder(
                padding: const EdgeInsets.all(8),
                itemCount: entries.length,
                itemBuilder: (BuildContext context, int index) {
                  return Container(
                      height: 50,
                      // child: Center(child: Text(' ${entries[index]}')),
                      child: Row(
                        children: [
                          Text(' ${entries[index]}'),
                          TextButton(
                            style: ButtonStyle(
                              foregroundColor:
                                  MaterialStateProperty.all<Color>(Colors.blue),
                            ),
                            onPressed: () => _check_bot(entries[index], index),
                            child: const Text('Check BOT'),
                          ),
                          Text(
                            Bots_r[index],
                            style: Theme.of(context).textTheme.bodyText1,
                          ),
                          TextButton(
                            style: ButtonStyle(
                              foregroundColor:
                                  MaterialStateProperty.all<Color>(Colors.blue),
                            ),
                            onPressed: () =>
                                _check_topic(entries[index], index),
                            child: const Text('See Topics'),
                          ),
                          Text(
                            Topics_r[index],
                            style: Theme.of(context).textTheme.bodyText1,
                          ),
                          TextButton(
                            style: ButtonStyle(
                              foregroundColor:
                                  MaterialStateProperty.all<Color>(Colors.blue),
                            ),
                            onPressed: () => _check_mood(entries[index], index),
                            child: const Text('See Moods'),
                          ),
                          Text(
                            Moods_r[index],
                            style: Theme.of(context).textTheme.bodyText1,
                          ),
                          TextButton(
                            style: ButtonStyle(
                              foregroundColor:
                                  MaterialStateProperty.all<Color>(Colors.blue),
                            ),
                            onPressed: () => _launchUrl(entries[index]),
                            child: const Text('see tweets'),
                          ),
                        ],
                      ));
                }),
          ),
          TextButton(
            style: ButtonStyle(
              foregroundColor: MaterialStateProperty.all<Color>(
                  Color.fromARGB(255, 243, 135, 12)),
            ),
            onPressed: _handleSignIn,
            child: const Text('Sign in with Google'),
          )
        ],
      ),

      //   floatingActionButton: FloatingActionButton(
      //     style: ButtonStyle(
      //                           foregroundColor:
      //                               MaterialStateProperty.all<Color>(Colors.blue),
      //                         ),
      //       onPressed: _handleSignIn,
      //       tooltip: 'Increment',
      //       child: const Text("Sign in with google")),
      //   // This trailing comma makes auto-formatting nicer for build methods.
    );
  }

  // /// Use Twitter API v2.
  // Future loginV2() async {
  //   // print('OS: ${Platform.macOS}');
  //   final twitterLogin = TwitterLogin(
  //     /// Consumer API keys
  //     apiKey: 'wf6vwqUsK59YJ3BxzRXViwTSA',

  //     /// Consumer API Secret keys
  //     apiSecretKey: 'ZxP55BZ2cXR0A0DOAjg5dqX9HWvpbBOie6ZES7euPfyESuIx7n',

  //     /// Registered Callback URLs in TwitterApp
  //     /// Android is a deeplink
  //     /// iOS is a URLScheme
  //     redirectURI: 'witterkit-wf6vwqUsK59YJ3BxzRXViwTSA://',
  //   );

  //   /// Forces the user to enter their credentials
  //   /// to ensure the correct users account is authorized.
  //   /// If you want to implement Twitter account switching, set [force_login] to true
  //   /// login(forceLogin: true);
  //   final authResult = await twitterLogin.loginV2();
  //   switch (authResult.status) {
  //     case TwitterLoginStatus.loggedIn:
  //       // success
  //       print('====== Login success ======');
  //       break;
  //     case TwitterLoginStatus.cancelledByUser:
  //       // cancel
  //       print('====== Login cancel ======');
  //       break;
  //     case TwitterLoginStatus.error:
  //     case null:
  //       // error
  //       print('====== Login error ======');
  //       break;
  //   }
  // }
}
