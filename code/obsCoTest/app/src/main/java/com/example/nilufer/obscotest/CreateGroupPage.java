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
import android.widget.EditText;

import org.json.JSONArray;
import org.json.JSONObject;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.MalformedURLException;
import java.net.URL;
import java.util.ArrayList;

public class CreateGroupPage extends AppCompatActivity {

    private static final String TAG = "RecycleViewAdapterCGP";

    private ArrayList<String> eligibleIDs = new ArrayList<>();
    private ArrayList<String> eligibleNames = new ArrayList<>();
    private ArrayList<String> recScores = new ArrayList<>();
    private ArrayList<String> skillIDs = new ArrayList<>();
    private ArrayList<Boolean> checkBoxAdd = new ArrayList<>();
    private ArrayList<Boolean> checkBoxLeader = new ArrayList<>();

    private String userID;
    String addID;
    String leaderID;
    String groupName;

    private class groupPageConnect extends AsyncTask {
        @Override
        protected Object doInBackground(Object... arg0) {

            try{
                System.out.println("Testing 1 - Send Http GET request");
                getEligibleMembers();

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
            initCreateGroupButton();
            // dismiss progress dialog here
            // into onPostExecute() but that is upto you
        }
    }

    private class createGroupConnect extends AsyncTask {
        @Override
        protected Object doInBackground(Object... arg0) {

            try{
                System.out.println("Testing 1 - Send Http GET request");
                String urlBase = "http://obsco.me/obsco/api/v1.0/";
                String createGroupUrl = urlBase + "creategroup/" + groupName + "/" + userID + "/" + addID;
                URL obj = new URL(createGroupUrl);;
                System.out.println (createGroupUrl);
                HttpURLConnection con = (HttpURLConnection) obj.openConnection();
                con.setRequestMethod("GET");
                con.setRequestProperty("User-Agent", "Mozilla/5.0");
                BufferedReader in = new BufferedReader(new InputStreamReader(con.getInputStream()));
                String inputLine;
                StringBuffer response = new StringBuffer();
                while ((inputLine = in.readLine()) != null) {
                    response.append(inputLine);
                }
                in.close();
                System.out.println("RESPONSE: ");
                System.out.println(response.toString());

                String addLeaderUrl = urlBase + "addleader/" + userID + "/" + leaderID;
                obj = new URL(addLeaderUrl);;
                System.out.println (addLeaderUrl);
                con = (HttpURLConnection) obj.openConnection();
                con.setRequestMethod("GET");
                con.setRequestProperty("User-Agent", "Mozilla/5.0");
                in = new BufferedReader(new InputStreamReader(con.getInputStream()));
                response = new StringBuffer();
                while ((inputLine = in.readLine()) != null) {
                    response.append(inputLine);
                }
                in.close();
                System.out.println("RESPONSE: ");
                System.out.println(response.toString());
            } catch (Exception e) {
                System.err.println("Oops!");
                e.printStackTrace();
            }
            return null;
        }

        @Override
        protected void onPostExecute(Object o) {

        }
    }

    private void getEligibleMembers() throws Exception {
        String url = "http://obsco.me/obsco/api/v1.0/recommender/" + userID + "/15/";
        if (skillIDs.size() == 0){
            url = url + "_";
        }else{
            url = url + skillIDs.get(0);
            for (int x = 1; x < skillIDs.size(); x++){
                url = url + "_" + skillIDs.get(x);
            }
        }

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
        JSONArray allContainingArray = reader.getJSONArray("recommendation");
        JSONObject temp;

        for ( int x = 0; x < allContainingArray.length(); x++){
            temp = allContainingArray.getJSONObject(x);
            eligibleIDs.add(temp.getString("id"));
            eligibleNames.add(temp.getString("name"));
            if (skillIDs.size() == 0)
                recScores.add("0");
            else
                recScores.add(temp.getString("recommended"));
            checkBoxLeader.add(false);
            checkBoxAdd.add(false);
        }
    }

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_create_group_page);
        Log.d(TAG, "started");
        try {
            CreateGroupPageInit();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    private void CreateGroupPageInit() throws Exception{
        Intent intent = getIntent();
        userID = intent.getStringExtra("userID");
        skillIDs = intent.getStringArrayListExtra("skillIDs");
        new groupPageConnect().execute();
    }

    private void initRecyclerView(){
        Log.d(TAG, "initializingRecyclerView");
        RecyclerView recyclerView = findViewById(R.id.recycler_view_new_group);
        RecyclerViewAdapterNewGroup adapter = new RecyclerViewAdapterNewGroup( this, eligibleNames, recScores, checkBoxAdd, checkBoxLeader);
        recyclerView.setAdapter(adapter);
        recyclerView.setLayoutManager( new LinearLayoutManager( this));
    }

    private void initCreateGroupButton(){
        Log.d(TAG, "initializingCreateGroupButton");
        Button confirmSkill = findViewById(R.id.button_create_group);
        final EditText groupNameText = findViewById(R.id.group_name_input);
        confirmSkill.setOnClickListener(new View.OnClickListener()
        {
            @Override
            public void onClick(View v)
            {
                addID = userID;
                leaderID = userID;
                for ( int x= 0; x < checkBoxAdd.size(); x++){
                    if ( checkBoxAdd.get(x)) {
                        addID = addID + "_" + eligibleIDs.get(x);
                    }
                }
                for ( int x= 0; x < checkBoxLeader.size(); x++){
                    if ( checkBoxLeader.get(x)) {
                        leaderID = leaderID + "_" + eligibleIDs.get(x);
                    }
                }
                groupName = groupNameText.getText().toString();
                new createGroupConnect().execute();
            }
        });

    }

}
