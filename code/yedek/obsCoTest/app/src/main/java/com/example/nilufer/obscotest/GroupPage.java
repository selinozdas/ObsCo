package com.example.nilufer.obscotest;

import android.content.Intent;
import android.os.AsyncTask;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.support.v7.widget.LinearLayoutManager;
import android.support.v7.widget.RecyclerView;
import android.util.Log;
import android.view.View;
import android.widget.Button;

import org.json.JSONArray;
import org.json.JSONObject;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.URL;
import java.util.ArrayList;

public class GroupPage extends AppCompatActivity {

    private static final String TAG = "RecycleViewAdapter";
    private ArrayList<String> groupIDs = new ArrayList<>();
    private ArrayList<String> groupNames = new ArrayList<>();
    private String userID;
    private String password;
    private String userName;

    private class groupPageConnect extends AsyncTask {
        @Override
        protected Object doInBackground(Object... arg0) {

            try{
                System.out.println("Testing 1 - Send Http GET request");
                getGroups();

            } catch (Exception e) {
                System.err.println("Oops!");
                e.printStackTrace();
            }
            return null;
        }

        @Override
        protected void onPostExecute(Object o) {
            //call what you want to update
            initRecyclerView();
            initNewGroupButton();
            initMainMenuButton();
            // dismiss progress dialog here
            // into onPostExecute() but that is upto you
        }
    }

    private void getGroups() throws Exception{

        String url = "http://obsco.me/obsco/api/v1.0/users/" + userID;
        URL obj = new URL(url);
        HttpURLConnection con = (HttpURLConnection) obj.openConnection();
        con.setRequestMethod("GET");
        con.setRequestProperty("User-Agent", "Mozilla/5.0");

        int responseCode = con.getResponseCode();
        System.out.println("Response Code  for IDs: " + responseCode);

        BufferedReader in = new BufferedReader(new InputStreamReader(con.getInputStream()));
        String inputLine;
        StringBuffer response = new StringBuffer();
        while ((inputLine = in.readLine()) != null) {
            response.append(inputLine);
        }
        in.close();

        JSONObject reader = new JSONObject(response.toString());
        JSONArray allContainingArray = reader.getJSONArray("users");
        JSONObject userJSON  = (JSONObject) allContainingArray.get(0);
        JSONArray temp = userJSON.getJSONArray("groups");

        for (int x = 0; x < temp.length(); x++){
            groupIDs.add(temp.getJSONObject(x).getString("id"));
            url = "http://obsco.me/obsco/api/v1.0/groupname/" + groupIDs.get(x);
            obj = new URL(url);
            con = (HttpURLConnection) obj.openConnection();
            con.setRequestMethod("GET");
            con.setRequestProperty("User-Agent", "Mozilla/5.0");

            responseCode = con.getResponseCode();
            System.out.println("Response Code  for IDs: " + responseCode);

            in = new BufferedReader(new InputStreamReader(con.getInputStream()));
            response = new StringBuffer();
            while ((inputLine = in.readLine()) != null) {
                response.append(inputLine);
            }
            in.close();

            reader = new JSONObject(response.toString());
            groupNames.add(reader.getString("name"));
        }

    }


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_group_page);
        Log.d(TAG, "started");
        try {
            groupPageInit();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    private void groupPageInit() throws Exception{
        Intent intent = getIntent();
        userID = intent.getStringExtra("ID_FROM_LOGIN");
        password = intent.getStringExtra("PASSWORD_FROM_LOGIN");
        userName = intent.getStringExtra("NAME_FROM_LOGIN");
        new groupPageConnect().execute();
        //initRecyclerView();
    }

    private void initRecyclerView(){
        Log.d(TAG, "initializingRecyclerView");
        RecyclerView recyclerView = findViewById(R.id.recycler_view);
        RecyclerViewAdapter adapter = new RecyclerViewAdapter( this, groupIDs, groupNames, userID, password, userName);
        recyclerView.setAdapter(adapter);
        recyclerView.setLayoutManager( new LinearLayoutManager( this));
    }

    private void initNewGroupButton(){
        Log.d(TAG, "initializingCreateGroupButton");
        Button createGroup = findViewById(R.id.button_new_group);
        createGroup.setOnClickListener(new View.OnClickListener()
        {
            @Override
            public void onClick(View v)
            {
                //Open new page
                Intent intent = new Intent("android.intent.action.SKILLLIST");
                intent.putExtra("ID_FROM_LOGIN", userID );
                intent.putExtra("NAME_FROM_LOGIN", userName);
                intent.putExtra("PASSWORD_FROM_LOGIN", password);
                startActivity(intent);
            }
        });
    }
    private void initMainMenuButton(){
        Log.d(TAG, "initializingCreateGroupButton");
        Button mainMenu = findViewById(R.id.button_main_menu);
        mainMenu.setOnClickListener(new View.OnClickListener()
        {
            @Override
            public void onClick(View v)
            {
                Intent intent = new Intent("android.intent.action.HOMEPAGE1");
                intent.putExtra("ID_FROM_LOGIN", userID);
                intent.putExtra("NAME_FROM_LOGIN", userName);
                intent.putExtra("PASSWORD_FROM_LOGIN", password);
                startActivity(intent);
            }
        });

    }
}