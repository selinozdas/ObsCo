package com.example.nilufer.obscotest;

import android.content.Intent;
import android.graphics.Bitmap;
import android.graphics.BitmapFactory;
import android.graphics.Color;
import android.os.AsyncTask;
import android.support.v4.graphics.drawable.RoundedBitmapDrawable;
import android.support.v4.graphics.drawable.RoundedBitmapDrawableFactory;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.text.Html;
import android.view.Gravity;
import android.view.View;
import android.view.ViewGroup;
import android.widget.Button;
import android.widget.ImageView;
import android.widget.LinearLayout;
import android.widget.TextView;
import android.widget.Toast;

import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.URL;
import java.util.Iterator;
import java.util.Map;
import java.util.Random;

public class voteSkillPage1 extends AppCompatActivity {
    // MAHIR
    String idFromGroupPage;
    String groupIdFromGroupPage;
    String age;
    String email;
    String id;
    String name;
    String password;
    String title;
    Double skillLevel;
    JSONArray skillsContainingArray;
    boolean isSuperuser;

    private ImageView voteButton;
    LinearLayout ll;
    int votedValue = 0;
    int votedSkillId = 0;
    String secondUserId;
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
            startActivity(intent);

            //Show the result obtained from doInBackground
        }

    }

    public void InitializeVoteButton()
    {
        voteButton = (ImageView)findViewById(R.id.add_vote);

        voteButton.setOnClickListener(new View.OnClickListener()
        {
            @Override
            public void onClick(View v)
            {
                new ConnectionTest().execute("");

                //Open new page
                /*
                Intent intent = new Intent("android.intent.action.ADDCOMMENTPAGE");
                intent.putExtra("ID_FROM_LOGIN", id);
                intent.putExtra("NAME_FROM_LOGIN", name);
                intent.putExtra("PASSWORD_FROM_LOGIN", password);
                startActivity(intent);
                */
            }
        });
    }

    private void sendGet() throws Exception {
        String url = "http://obsco.me/obsco/api/v1.0/voteskill/" + secondUserId + "/" + votedSkillId + "/" + votedValue;
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
        System.out.println("TATATA VOTE RESPONSE : " + responseCode);

        BufferedReader in = new BufferedReader(
                new InputStreamReader(con.getInputStream()));
        String inputLine;
        StringBuffer response = new StringBuffer();
        while ((inputLine = in.readLine()) != null) {
            response.append(inputLine);
        }
        in.close();
/*
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
        email = userJSON.getString("email");

        TextView nameText = (TextView) findViewById(R.id.personnel_name);
        nameText.setText(name);
        */
    }

/*
    public LinearLayout addSkillLayout(String s)
    {
        final LinearLayout newLayout = new LinearLayout(this);
        newLayout.setLayoutParams(new ViewGroup.LayoutParams(LinearLayout.LayoutParams.MATCH_PARENT, LinearLayout.LayoutParams.WRAP_CONTENT));
        newLayout.setOrientation(LinearLayout.HORIZONTAL);
        //newLayout.setGravity(Gravity.);
        newLayout.addView( makeImageView1(R.drawable.ball3,125) );
        newLayout.addView( makeTextView(s) );

        final ImageView plusImage = makeImageView1(R.drawable.plus2, 200);
        newLayout.addView( plusImage );

        final String skillN = s;
        plusImage.setOnClickListener(new View.OnClickListener()
        {
            @Override
            public void onClick(View v)
            {

                Intent intent = new Intent("android.intent.action.VOTESKILLPAGE");
                intent.putExtra("ID_FROM_LOGIN", id);
                intent.putExtra("NAME_FROM_LOGIN", name);
                intent.putExtra("PASSWORD_FROM_LOGIN", password);
                intent.putExtra("SKILL_NAME_FROM_PROFILE", skillN);
                startActivity(intent);

            }
        });

        //newLayout.addView( makeTextView("! ! ! ! ! ! ! ! ! !"));
        return newLayout;
    }
*/
    public LinearLayout makeStarsLayout(int cnt)
    {
        final LinearLayout newLayout = new LinearLayout(this);
        LinearLayout.LayoutParams newLayoutParams = new LinearLayout.LayoutParams(
                LinearLayout.LayoutParams.MATCH_PARENT, LinearLayout.LayoutParams.WRAP_CONTENT);
        newLayout.setLayoutParams(newLayoutParams);
        newLayout.setOrientation(LinearLayout.HORIZONTAL);
        //newLayout.setGravity(Gravity.CENTER);
        for(int i=0; i<cnt; i++)
        {
            newLayout.addView( makeImageView1(R.drawable.star40blue,100, i) );
        }
        for(int i=cnt; i<10; i++)
        {
            newLayout.addView( makeImageView1(R.drawable.star40gray,100, i) );
        }
        //newLayout.addView( makeTextView("   " + skillLevel.toString()) );
        return newLayout;
    }

    public ImageView makeImageView1(int resourceName, int widthToUse, int imageId)
    {
        LinearLayout.LayoutParams layoutParams=new LinearLayout.LayoutParams(new ViewGroup.LayoutParams(widthToUse, LinearLayout.LayoutParams.WRAP_CONTENT));
        layoutParams.gravity=Gravity.CENTER;
        final ImageView newImage = new ImageView(this);
        newImage.setImageResource(resourceName);
        newImage.setLayoutParams(layoutParams);
        newImage.setId(imageId);

        newImage.setOnClickListener(new View.OnClickListener()
        {
            @Override
            public void onClick(View v)
            {
                ll.removeAllViews();
                votedValue = newImage.getId();
                votedValue = votedValue + 1;
                ll.addView( makeStarsLayout(votedValue) );
            }
        });
        return newImage;
    }
    public TextView makeTextView(String s)
    {
        final TextView nameTextView = new TextView(this);
        nameTextView.setText(s);
        nameTextView.setTextSize(20);
        nameTextView.setBackgroundColor( Color.argb(255,255,255,255) );
        nameTextView.setTextAppearance(this, R.style.Widget_AppCompat_Button_Borderless);
        nameTextView.setGravity(Gravity.CENTER);
        nameTextView.setMinimumHeight(175);
        //nameTextView.setLayoutParams(new ViewGroup.LayoutParams(LinearLayout.LayoutParams.MATCH_PARENT, LinearLayout.LayoutParams.WRAP_CONTENT));
        return nameTextView;
    }
// MAHIR






    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_vote_skill_page1);
        ll = (LinearLayout)findViewById(R.id.texts_layout);
        /////
        id = getIntent().getStringExtra("ID_FROM_LOGIN");
        name = getIntent().getStringExtra("NAME_FROM_LOGIN");
        password = getIntent().getStringExtra("PASSWORD_FROM_LOGIN");
        secondUserId = getIntent().getStringExtra("secondUserID");
        votedSkillId = getIntent().getIntExtra("SKILLID",0);
        ll.addView(makeStarsLayout(0));
        InitializeVoteButton();



        //addUserTraits();
    }
}
