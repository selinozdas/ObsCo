package com.example.nilufer.obscotest;

import android.Manifest;
import android.content.Intent;
import android.content.pm.PackageManager;
import android.os.AsyncTask;
import android.support.v4.app.ActivityCompat;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.*;

import org.json.JSONArray;
import org.json.JSONObject;

import java.io.BufferedReader;
import java.io.DataOutputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.HttpURLConnection;
import java.net.InetAddress;
import java.net.Socket;
import java.net.URL;
import java.net.URLConnection;
import java.net.UnknownHostException;



public class homeActivity1 extends AppCompatActivity {
// MAHIR
private Button profilButton;
private Button testButton;
private Button gruplarimButton;
static Socket socket = null;

String age;
String email;
String id;
String name;
String password;
String title;
boolean isSuperuser;


    private class ConnectionTest extends AsyncTask {
        @Override
        protected Object doInBackground(Object... arg0) {

            try{
                System.out.println("Testing 1 - Send Http GET request");
                sendGet();
                //sendPost();


            } catch (Exception e) {
                System.err.println("Oops!");
                e.printStackTrace();
            }
            return null;
        }
    }

/*
Thread thread = new Thread(new Runnable() {

    @Override
    public void run() {
        try  {
            System.out.println("THREAD WORKING AFTER 5 SECS");
            sendingGetRequest();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
});
    */

    /**
    // HTTP GET request
    private void sendingGetRequest() throws Exception {

        String urlString = "http://127.0.0.1:5000/obsco/api/v1.0/users";

        URL url = new URL(urlString);
        HttpURLConnection con = (HttpURLConnection) url.openConnection();

        // By default it is GET request
        con.setRequestMethod("GET");

        //add request header
        con.setRequestProperty("User-Agent", "Mozilla/5.0");
        System.out.println("POINT 1");
        //PROBLEM AREA
        //////////////
        // Storage Permissions
        final int REQUEST_EXTERNAL_STORAGE = 1;
        String[] PERMISSIONS_STORAGE = {
                Manifest.permission.READ_EXTERNAL_STORAGE,
                Manifest.permission.WRITE_EXTERNAL_STORAGE
        };
        // Check if we have write permission
        int permission = ActivityCompat.checkSelfPermission( this, Manifest.permission.WRITE_EXTERNAL_STORAGE);

        if (permission != PackageManager.PERMISSION_GRANTED) {
            // We don't have permission so prompt the user
            ActivityCompat.requestPermissions(
                    this,
                    PERMISSIONS_STORAGE,
                    REQUEST_EXTERNAL_STORAGE
            );
        }
        System.out.println("BOING");
        int responseCode = con.getResponseCode();
        //////////////
        //PROBLEM AREA END
        System.out.println("DOING DOING DOING");
        System.out.println("Sending get request : "+ url);
        //System.out.println("Response code : "+ responseCode);


        // Reading response from input Stream
        BufferedReader in = new BufferedReader(
                new InputStreamReader(con.getInputStream()));
        String output;
        StringBuffer response = new StringBuffer();

        while ((output = in.readLine()) != null) {
            response.append(output);
        }
        in.close();

        //printing result from response
        System.out.println(response.toString());

    }
    */
    // HTTP POST request
    private void sendPost() throws Exception {

        String url = "http://obsco.me/obsco/api/v1.0/skills/addskill/12345671/androiddev";
        //String url = "http://obsco.me/obsco/api/v1.0/reputation/12345671";
        //url = url + id + "/" + "androiddev";
        URL obj = new URL(url);
        HttpURLConnection con = (HttpURLConnection) obj.openConnection();

        //add reuqest header
        con.setRequestMethod("POST");
        con.setRequestProperty("User-Agent", "Mozilla/5.0");
        //con.setRequestProperty("Accept-Language", "en-US,en;q=0.5");

        String urlParameters = "dogancan";
        /*
        // Send post request
        con.setDoOutput(true);
        DataOutputStream wr = new DataOutputStream(con.getOutputStream());
        wr.writeBytes(urlParameters);
        wr.flush();
        wr.close();
        */
        int responseCode = con.getResponseCode();
        System.out.println("\nSending 'POST' request to URL : " + url);
        System.out.println("Post parameters : " + urlParameters);
        System.out.println("Response Code : " + responseCode);

        BufferedReader in = new BufferedReader(
                new InputStreamReader(con.getInputStream()));
        String inputLine;
        StringBuffer response = new StringBuffer();

        while ((inputLine = in.readLine()) != null) {
            response.append(inputLine);
        }
        in.close();

        //print result
        System.out.println("MY RESPONSE IS:");
        System.out.println(response.toString());

    }

    private void sendGet() throws Exception {

        System.out.println("DEBUG POINT 1: ");
        //String url = "http://obsco.me/obsco/api/v1.0/skills/addskill/dogancan"; //"http://127.0.0.1:5000/obsco/api/v1.0/users";
        //String url = "http://obsco.me/obsco/api/v1.0/addskill/androiddev";
        String url = "http://obsco.me/obsco/api/v1.0/skills/21400537";

        //String url = "http://obsco.me/obsco/api/v1.0/reputation/12345671";
        URL obj = new URL(url);
        HttpURLConnection con = (HttpURLConnection) obj.openConnection();
        System.out.println("DEBUG POINT 2: ");
        // optional default is GET
        con.setRequestMethod("GET");
        System.out.println("DEBUG POINT 3: ");
        //add request header
        //con.setRequestProperty("User-Agent",);
        con.setRequestProperty("User-Agent", "Mozilla/5.0");

        int responseCode = con.getResponseCode();
        System.out.println("DEBUG POINT 4: ");
        System.out.println("\nSending 'GET' request to URL : " + url);
        System.out.println("Response Code : " + responseCode);

        BufferedReader in = new BufferedReader(
                new InputStreamReader(con.getInputStream()));
        String inputLine;
        StringBuffer response = new StringBuffer();
        int cntTest1 = 0;
        while ((inputLine = in.readLine()) != null) {
            response.append(inputLine);
            cntTest1++;
            System.out.println(cntTest1);
        }
        in.close();

        //print result
        System.out.println("RESPONSE: ");
        System.out.println(response.toString());
        /*
        JSONObject reader = new JSONObject(response.toString());

        JSONArray allContainingArray = reader.getJSONArray("users");
        JSONObject userJSON  = (JSONObject)allContainingArray.get(0); //reader.getJSONObject("users");
        age = userJSON.getString("age");
        email = userJSON.getString("email");
        id = userJSON.getString("id");
        name = userJSON.getString("name");
        password = userJSON.getString("password");
        title = userJSON.getString("title");
        System.out.println("AGE: ");
        System.out.println(age);

        setName();
        */
    }

    public void setName()
    {
        TextView testNameView = (TextView) findViewById(R.id.homeNameView);

        //Toast.makeText(homeActivity1.this, "NAME: " + name, Toast.LENGTH_LONG).show();
        testNameView.setText(name); //set text for text view
    }

    public void InitializeTestButton() throws UnknownHostException, IOException
    {

        testButton = (Button)findViewById(R.id.testbutton);

        testButton.setOnClickListener(new View.OnClickListener()
        {
            @Override
            public void onClick(View v)
            {
                //FIND THIS FROM DATABASE
                //usernameFieldInput.getText().toString()
                //MATCH WITH PASSWORD
                //passwordFieldInput.getText().toString()

                /////Log.d("myTag", "This is my message");
                String testString = "TESTOOOOOOOO";
                Toast.makeText(homeActivity1.this, testString, Toast.LENGTH_LONG).show();

                //Open new page
                Intent intent = new Intent("android.intent.action.SECONDPROFILEPAGE");
                intent.putExtra("ID_FROM_LOGIN", id);
                intent.putExtra("NAME_FROM_LOGIN", name);
                intent.putExtra("PASSWORD_FROM_LOGIN", password);
                startActivity(intent);
            }
        });

        //URL oracle = new URL("http://127.0.0.1:5000/"); //http://localhost:8080
        //URLConnection yc = oracle.openConnection();

        /**
         BufferedReader in = new BufferedReader(new InputStreamReader(yc.getInputStream()));
         String inputLine;
         while ((inputLine = in.readLine()) != null)
         System.out.println(inputLine);
         in.close();
         */
    }

    public void InitializeProfilButton() throws UnknownHostException, IOException
    {

        profilButton = (Button)findViewById(R.id.profilbutton);

        profilButton.setOnClickListener(new View.OnClickListener()
        {
            @Override
            public void onClick(View v)
            {
                //FIND THIS FROM DATABASE
                //usernameFieldInput.getText().toString()
                //MATCH WITH PASSWORD
                //passwordFieldInput.getText().toString()

                /////Log.d("myTag", "This is my message");
                String testString = "profil button clicked";
                Toast.makeText(homeActivity1.this, testString, Toast.LENGTH_LONG).show();

                //Open new page
                Intent intent = new Intent("android.intent.action.PROFILEPAGE");
                intent.putExtra("ID_FROM_LOGIN", id);
                intent.putExtra("NAME_FROM_LOGIN", name);
                intent.putExtra("PASSWORD_FROM_LOGIN", password);
                startActivity(intent);
            }
        });

        //URL oracle = new URL("http://127.0.0.1:5000/"); //http://localhost:8080
        //URLConnection yc = oracle.openConnection();

        /**
        BufferedReader in = new BufferedReader(new InputStreamReader(yc.getInputStream()));
        String inputLine;
        while ((inputLine = in.readLine()) != null)
            System.out.println(inputLine);
        in.close();
         */
    }

    public void InitializeGruplarimButton()
    {
        profilButton = (Button)findViewById(R.id.gruplarimbutton);

        profilButton.setOnClickListener(new View.OnClickListener()
        {
            @Override
            public void onClick(View v)
            {

                String testString = "Berkin sayfası açıldı";
                Toast.makeText(homeActivity1.this, testString, Toast.LENGTH_LONG).show();

                //Open new page
                Intent intent = new Intent("android.intent.action.GROUP");
                intent.putExtra("ID_FROM_LOGIN", id);
                intent.putExtra("NAME_FROM_LOGIN", name);
                intent.putExtra("PASSWORD_FROM_LOGIN", password);
                startActivity(intent);
            }
        });
    }
// MAHIR

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_home1);

        ///////
        id = getIntent().getStringExtra("ID_FROM_LOGIN");
        name = getIntent().getStringExtra("NAME_FROM_LOGIN");
        password = getIntent().getStringExtra("PASSWORD_FROM_LOGIN");
        setName();
        try {
            InitializeTestButton();
        } catch (IOException e) {
            e.printStackTrace();
        }

        try {
            InitializeProfilButton();

        } catch (IOException e) {
            e.printStackTrace();
            System.out.println("PROFIL ERROR");
        }




        new ConnectionTest().execute("");

/*
        try
        {
            System.out.println("5 SANIYE ONCESI");
            thread.sleep(5000);
            System.out.println("5 SANIYE SONRASI");
            thread.start();
        }
        catch(InterruptedException ex)
        {
            Thread.currentThread().interrupt();
        }
*/


        InitializeGruplarimButton();
    }
}
