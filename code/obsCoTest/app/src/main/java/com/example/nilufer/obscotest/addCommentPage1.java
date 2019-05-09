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
import java.util.ArrayList;
import java.util.List;

public class addCommentPage1 extends AppCompatActivity {
    private EditText passwordFieldInput, textFieldInput;
    private ImageButton tamamlaButton;

    String id;
    String password;
    String inputPassword;
    String name;
    String secondUserId = "21400537";
    String sentimentString = "";
    String groupID;
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

        @Override
        protected void onPostExecute(Object o) {
            //Open new page

            Intent intent = new Intent("android.intent.action.SECONDPROFILEPAGE");

            intent.putExtra("ID_FROM_LOGIN", id);
            intent.putExtra("NAME_FROM_LOGIN", name);
            intent.putExtra("PASSWORD_FROM_LOGIN", password);
            intent.putExtra("secondUserID", secondUserId);
            intent.putExtra("groupID", groupID);

            startActivity(intent);

            //Show the result obtained from doInBackground
        }

    }

    private String buildSentimentString()
    {
        //List<String> words = new ArrayList<>();
        TextView temp = (TextView)findViewById(R.id.sentimentText);
        sentimentString = temp.getText().toString();
        String[] splited = sentimentString.split("\\s+");

        String urlString = splited[0];
        for(int i=1; i<splited.length; i++)
        {
            urlString = urlString + "_";
            urlString = urlString + splited[i];
            System.out.println(splited[i]);
        }
        System.out.println("SENTIMENT URL STRING: ");
        System.out.println(urlString);
        return urlString;
    }
    private void sendGet() throws Exception {
        //String url = "http://obsco.me/obsco/api/v1.0/users/" + id;
        String url = "http://obsco.me/obsco/api/v1.0/sentiment/" + id + "/" + secondUserId + "/";
        url = url + buildSentimentString();
        System.out.println("DEBUG POINT 1: ");
        System.out.println(id);
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
/*
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
            startActivity(intent);
        }
*/
    }

    public void TamamlaButton()
    {
        textFieldInput = (EditText)findViewById(R.id.sentimentText);
        passwordFieldInput = (EditText)findViewById(R.id.password1);
        tamamlaButton = (ImageButton)findViewById(R.id.tamamlabutton);

        tamamlaButton.setOnClickListener(new View.OnClickListener()
        {
            @Override
            public void onClick(View v)
            {
                System.out.println("TAMAMLA BENI:");
                inputPassword = passwordFieldInput.getText().toString();

                new ConnectionTest().execute("");
                if(password.equalsIgnoreCase(inputPassword))
                {

                    System.out.println("SIFRELER AYNI");

                }

            }
        });
    }

    @Override
    protected void onCreate(Bundle savedInstanceState)
    {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_add_comment_page1);

        id = getIntent().getStringExtra("ID_FROM_LOGIN");
        name = getIntent().getStringExtra("NAME_FROM_LOGIN");
        password = getIntent().getStringExtra("PASSWORD_FROM_LOGIN");
        secondUserId = getIntent().getStringExtra("secondUserID");
        groupID = getIntent().getStringExtra("groupID");
        TamamlaButton();

    }

}