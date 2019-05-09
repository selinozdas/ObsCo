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

public class SkillListPage extends AppCompatActivity {

    private static final String TAG = "RecycleViewAdapterSL";
    private ArrayList<String> skillIDs = new ArrayList<>();
    private ArrayList<String> skillNames = new ArrayList<>();
    private ArrayList<Boolean> checkBoxes = new ArrayList<>();
    private String userID;

    private ArrayList<String> skillIDsOutput = new ArrayList<>();

    private class skillListConnect extends AsyncTask {
        @Override
        protected Object doInBackground(Object... arg0) {

            try{
                System.out.println("Testing 1 - Send Http GET request");
                getSkills();

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
            initConfirmButton();
            // dismiss progress dialog here
            // into onPostExecute() but that is upto you
        }
    }

    private void getSkills() throws Exception{
        String url = "http://obsco.me/obsco/api/v1.0/skilllist";
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
        JSONArray readerArray = reader.getJSONArray("skills");
        JSONObject temp;

        for (int x = 0; x < readerArray.length(); x++) {
            temp = readerArray.getJSONObject(x);
            System.out.println(temp.getString("id"));
            System.out.println(temp.getString("name"));
            skillIDs.add(temp.getString("id"));
            skillNames.add(temp.getString("name"));
            checkBoxes.add(false);
        }

    }

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_skill_list_page);
        Log.d(TAG, "started");
        try {
            skillListInit();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    private void skillListInit() throws Exception{
        Intent intent = getIntent();
        userID = intent.getStringExtra("userID");
        new skillListConnect().execute();
    }

    private void initRecyclerView(){
        Log.d(TAG, "initializingRecyclerView");
        RecyclerView recyclerView = findViewById(R.id.recycler_view_skill_list);
        RecyclerViewAdapterSkillList adapter = new RecyclerViewAdapterSkillList( this, skillNames, checkBoxes);
        recyclerView.setAdapter(adapter);
        recyclerView.setLayoutManager( new LinearLayoutManager( this));

    }

    private void initConfirmButton() {
        Log.d(TAG, "initializingCreateGroupButton");
        Button confirmSkill = findViewById(R.id.button_confirm_skills);
        confirmSkill.setOnClickListener(new View.OnClickListener()
        {
            @Override
            public void onClick(View v)
            {
                for ( int x= 0; x < skillIDs.size(); x++){
                    if ( checkBoxes.get(x)) {
                        System.out.println(skillIDs.get(x));
                        skillIDsOutput.add(skillIDs.get(x));
                    }
                }
                //Open new page
                Intent intent = new Intent("android.intent.action.CREATEGROUP");
                intent.putExtra("userID", userID );
                intent.putExtra("skillIDs", skillIDsOutput );
                startActivity(intent);
            }
        });

    }

}
