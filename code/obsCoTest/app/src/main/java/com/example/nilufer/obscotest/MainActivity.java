package com.example.nilufer.obscotest;

import android.content.Intent;
import android.os.AsyncTask;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.*;

import org.json.JSONArray;
import org.json.JSONObject;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.URL;

public class MainActivity extends AppCompatActivity {
        private EditText passwordFieldInput, usernameFieldInput;
        private ImageButton loginButton;

        String id;
        String password;
        String inputPassword;
        String name;
        boolean correctLoginInfo = false;

        private class ConnectionTest extends AsyncTask {
                @Override
                protected Object doInBackground(Object... arg0) {

                        try{
                                System.out.println("Testing 1 - Send Http GET request");
                                sendGet();

                        } catch (Exception e) {
                                System.err.println("Oops!");
                                e.printStackTrace();
                        }
                        return null;
                }
        }

        private void sendGet() throws Exception {
                String url = "http://obsco.me/obsco/api/v1.0/users/" + id;
                System.out.println("DEBUG POINT 1: ");
                //String url = "http://obsco.me/obsco/api/v1.0/users/12345671"; //"http://127.0.0.1:5000/obsco/api/v1.0/users";

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

                JSONObject reader = new JSONObject(response.toString());

                System.out.println("DEBUG POINT 5:");
                JSONArray allContainingArray = reader.getJSONArray("users");
                JSONObject userJSON  = (JSONObject)allContainingArray.get(0);// reader.getJSONObject("users");

                //UGETJSON ARR

                id = userJSON.getString("id");
                System.out.println("DEBUG POINT 6:" + id);
                name = userJSON.getString("name");
                password = userJSON.getString("password");

                System.out.println(id);
                System.out.println(password);
                System.out.println(inputPassword);
                //UNCOMMENT THIS ON PRODUCT
                if(password.equalsIgnoreCase(inputPassword))
                {
                        System.out.println("SIFRELER AYNI");
                        //Open new page
                        Intent intent = new Intent("android.intent.action.HOMEPAGE1");
                        intent.putExtra("ID_FROM_LOGIN", id);
                        intent.putExtra("NAME_FROM_LOGIN", name);
                        intent.putExtra("PASSWORD_FROM_LOGIN", password);
                        startActivity(intent);
                }

        }

public void LoginButton()
{
        usernameFieldInput = (EditText)findViewById(R.id.kullaniciadi1);
        passwordFieldInput = (EditText)findViewById(R.id.password1);
        loginButton = (ImageButton)findViewById(R.id.button);

        loginButton.setOnClickListener(new View.OnClickListener()
        {
                @Override
                public void onClick(View v)
                {
                        //FIND THIS FROM DATABASE
                        //usernameFieldInput.getText().toString()
                        //MATCH WITH PASSWORD
                        //passwordFieldInput.getText().toString()

                        /////Log.d("myTag", "This is my message");

                        //DEBUG TEXT
                        //String testString = "AAAAAAAATest";
                        //Toast.makeText(MainActivity.this, testString, Toast.LENGTH_LONG).show();
                        id = usernameFieldInput.getText().toString();
                        inputPassword = passwordFieldInput.getText().toString();
                        new ConnectionTest().execute("");
                }
        });
}

@Override
protected void onCreate(Bundle savedInstanceState)
        {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        LoginButton();

        }

}