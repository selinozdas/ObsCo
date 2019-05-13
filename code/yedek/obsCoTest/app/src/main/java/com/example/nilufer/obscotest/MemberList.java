package com.example.nilufer.obscotest;

import android.content.Intent;
import android.os.AsyncTask;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.support.v7.widget.LinearLayoutManager;
import android.support.v7.widget.RecyclerView;
import android.util.Log;
import android.widget.TextView;

import org.json.JSONArray;
import org.json.JSONObject;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.URL;
import java.util.ArrayList;

public class MemberList extends AppCompatActivity {

    private static final String TAG = "RecycleViewAdapter";
    private ArrayList<String> memberIDs = new ArrayList<>();
    private ArrayList<String> memberNames = new ArrayList<>();
    private String groupID;
    private String userID;
    private String password;
    private String userName;

    private class memberListConnect extends AsyncTask {
        @Override
        protected Object doInBackground(Object... arg0) {

            try{
                System.out.println("Testing 1 - Send Http GET request");
                getMembers();
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
            // dismiss progress dialog here
            // into onPostExecute() but that is upto you
        }
    }

    private void getMembers() throws Exception{
        String url = "http://obsco.me/obsco/api/v1.0/groupmembers/" + groupID;
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
        JSONArray allContainingArray = reader.getJSONArray("members");
        JSONObject temp;

        for (int x = 0; x < allContainingArray.length(); x++){
            temp = allContainingArray.getJSONObject(x);
            System.out.println (temp.getString("id"));
            System.out.println (temp.getString("name"));
            memberIDs.add(temp.getString("id"));
            memberNames.add(temp.getString("name"));
        }
    }

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_member_list);
        Log.d(TAG, "started");
        try {
            memberListInit();
        } catch (Exception e) {
            e.printStackTrace();
        }

    }


    private void memberListInit() throws Exception{
        Intent intent = getIntent();
        groupID = intent.getStringExtra("groupID");
        userID = intent.getStringExtra("ID_FROM_LOGIN");
        password = intent.getStringExtra("password");
        userName = intent.getStringExtra("userName");
        new memberListConnect().execute();
        //initRecyclerView();
    }

    private void initRecyclerView(){
        Log.d(TAG, "initializingRecyclerView");
        RecyclerView recyclerView = findViewById(R.id.recycler_view_members);
        RecyclerViewAdapterMembers adapter = new RecyclerViewAdapterMembers( this, memberIDs, memberNames,
                groupID, userID, userName, password);
        recyclerView.setAdapter(adapter);
        recyclerView.setLayoutManager( new LinearLayoutManager( this));
    }
}