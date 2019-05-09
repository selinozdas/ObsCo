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
import android.util.Log;
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
import java.io.InputStream;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.URL;
import java.util.Iterator;
import java.util.Map;
import java.util.Random;



public class profilePage1 extends AppCompatActivity {
    // MAHIR
    String idFromGroupPage;
    String groupIdFromGroupPage;
    String age;
    String email;
    String id;
    String secondUserId;
    String name;
    String password;
    String title;
    Double skillLevel;
    JSONArray skillsContainingArray;
    boolean isSuperuser;

    private ImageView addCommentButton;
    LinearLayout ll;
    ImageView bmImage;
    private class DownloadImageTask extends AsyncTask<String, Void, Bitmap> {

        protected Bitmap doInBackground(String... urls) {
            String urldisplay = urls[0];
            Bitmap bmp = null;
            try {
                InputStream in = new java.net.URL(urldisplay).openStream();
                bmp = BitmapFactory.decodeStream(in);
            } catch (Exception e) {
                Log.e("Error", e.getMessage());
                e.printStackTrace();
            }
            return bmp;
        }
        protected void onPostExecute(Bitmap result) {
            bmImage.setImageBitmap(result);
        }
    }

    private class ConnectionTest extends AsyncTask {
        @Override
        protected Object doInBackground(Object... arg0) {

            try{
                System.out.println("Testing 1 - Send Http GET request");
                getReputation();
                sendGet();
                //getUserData();
                getSkillsResponse();

            } catch (Exception e) {
                System.err.println("Oops!");
                e.printStackTrace();
            }
            return null;
        }

        @Override
        protected void onPostExecute(Object o) {


            ll.addView(makeTextView("İletişim: "+email));
            for (int i=0; i<skillsContainingArray.length(); i++)
            {
                String skillName;
                try {
                    JSONObject testObject = (JSONObject) skillsContainingArray.get(i);
                    skillName = testObject.getString("name");//skillsArray.getString(i);
                    skillLevel = testObject.getDouble("value");
                    int skillId = testObject.getInt("id");


                    ll.addView( addSkillLayout( skillName, skillId ) );//THIS HAS TO BE ONLY SKILL NAME NOW // + "\n " + skillLevel) );
                    ll.addView( makeStarsLayout() );

                } catch (JSONException e) {
                    e.printStackTrace();
                }

            }
            //addUserTraits();
            //Show the result obtained from doInBackground
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
        while ((inputLine = in.readLine()) != null) {
            response.append(inputLine);
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
        email = userJSON.getString("email");

        TextView nameText = (TextView) findViewById(R.id.personnel_name);
        nameText.setText(name);

        TextView titleText = (TextView) findViewById(R.id.first_trait);
        title = userJSON.getString("title");
        titleText.setText(title);


    }

    private void getSkillsResponse() throws Exception {

        System.out.println("DEBUG POINT 1: ");
        //String url = "http://obsco.me/obsco/api/v1.0/skills/addskill/dogancan"; //"http://127.0.0.1:5000/obsco/api/v1.0/users";
        //String url = "http://obsco.me/obsco/api/v1.0/addskill/androiddev";
        String url = "http://obsco.me/obsco/api/v1.0/skills/";
        url = url + id;
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

        while ((inputLine = in.readLine()) != null) {
            response.append(inputLine);
        }
        in.close();

        //print result
        System.out.println("RESPONSE: ");
        System.out.println(response.toString());

        JSONObject reader = new JSONObject(response.toString());

        skillsContainingArray = reader.getJSONArray("skills");
        JSONObject skillJSON  = (JSONObject)skillsContainingArray.get(1);
        System.out.println(skillJSON.getString("name"));
        System.out.println("DEB1: ");



        //skillsArray = (JSONArray) userJSON.get("skills");
        //System.out.println("LENGTHXD: ");
        //System.out.println(skillsArray.length());
    }


    private void getUserData() throws Exception {

        System.out.println("DEBUG POINT 1: ");
        String url = "http://obsco.me/obsco/api/v1.0/users/"; //"http://127.0.0.1:5000/obsco/api/v1.0/users";
        url = url + id;
        URL obj = new URL(url);
        HttpURLConnection con = (HttpURLConnection) obj.openConnection();
        // optional default is GET
        con.setRequestMethod("GET");
        //add request header
        //con.setRequestProperty("User-Agent",);
        con.setRequestProperty("User-Agent", "Mozilla/5.0");

        int responseCode = con.getResponseCode();
        System.out.println("\nSending 'GET' request to URL : " + url);
        System.out.println("Response Code : " + responseCode);

        BufferedReader in = new BufferedReader(
                new InputStreamReader(con.getInputStream()));
        String inputLine;
        StringBuffer response = new StringBuffer();

        in.close();

        //print result
        System.out.println("RESPONSE: ");
        System.out.println(response.toString());

        JSONObject reader = new JSONObject(response.toString());
/*
        //JSONObject userJSON  = reader.getJSONObject("users");
        JSONArray allContainingArray = reader.getJSONArray("users");
        JSONObject userJSON  = (JSONObject)allContainingArray.get(0);// reader.getJSONObject("users");

        email = userJSON.getString("email");
        name = userJSON.getString("name");
*/
        TextView nameText = (TextView) findViewById(R.id.personnel_name);

        //String text = "This is <font color='red'>red</font>. This is <font color='blue'>blue</font>.";
        //if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.N) {
        //    nameText.setText(Html.fromHtml(text,  Html.FROM_HTML_MODE_LEGACY), TextView.BufferType.SPANNABLE);
        //} else {
        //nameText.setText(Html.fromHtml(text), TextView.BufferType.SPANNABLE);
        //}


        //nameText.setText(name + " \nBEHAVIOR SCORE");

    }

    private void setNameAndEmail()
    {

    }

    private void getReputation() throws Exception {

        String url = "http://obsco.me/obsco/api/v1.0/reputation/"; //"http://127.0.0.1:5000/obsco/api/v1.0/users";
        url = url + id;
        URL obj = new URL(url);
        HttpURLConnection con = (HttpURLConnection) obj.openConnection();

        // optional default is GET
        con.setRequestMethod("GET");

        //add request header
        con.setRequestProperty("User-Agent", "Mozilla/5.0");

        int responseCode = con.getResponseCode();

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
        Double reputationValue = reader.getDouble("reputation");
        TextView reputationText = (TextView) findViewById(R.id.second_trait);
        reputationText.setText(reputationValue.toString() + " \nDAVRANIŞ PUANI");


    }

    public LinearLayout addSkillLayout(String s, int thisSkillId)
    {
        final LinearLayout newLayout = new LinearLayout(this);
        newLayout.setLayoutParams(new ViewGroup.LayoutParams(LinearLayout.LayoutParams.MATCH_PARENT, LinearLayout.LayoutParams.WRAP_CONTENT));
        newLayout.setOrientation(LinearLayout.HORIZONTAL);
        //newLayout.setGravity(Gravity.);
        newLayout.addView( makeImageView1(R.drawable.ball3,125) );
        newLayout.addView( makeTextView(s) );

/*        final ImageView plusImage = makeImageView1(R.drawable.plus2, 200);
        newLayout.addView( plusImage );
        final int tempSkillId = thisSkillId;

        plusImage.setOnClickListener(new View.OnClickListener()
        {
            @Override
            public void onClick(View v)
            {

                Intent intent = new Intent("android.intent.action.VOTESKILLPAGE");
                intent.putExtra("ID_FROM_LOGIN", id);
                intent.putExtra("NAME_FROM_LOGIN", name);
                intent.putExtra("PASSWORD_FROM_LOGIN", password);
                intent.putExtra("SKILLID", tempSkillId);
                //intent.putExtra("secondUserID", secondUserId);
                startActivity(intent);

            }
        });
*/
        //newLayout.addView( makeTextView("! ! ! ! ! ! ! ! ! !"));
        return newLayout;
    }

    public LinearLayout makeStarsLayout()
    {
        final LinearLayout newLayout = new LinearLayout(this);
        LinearLayout.LayoutParams newLayoutParams = new LinearLayout.LayoutParams(
                LinearLayout.LayoutParams.MATCH_PARENT, LinearLayout.LayoutParams.WRAP_CONTENT);
        newLayoutParams.leftMargin = 125;
        newLayout.setLayoutParams(newLayoutParams);
        newLayout.setOrientation(LinearLayout.HORIZONTAL);
        //newLayout.setGravity(Gravity.CENTER);
        for(int i=1; i<skillLevel; i++)
        {
            newLayout.addView( makeImageView1(R.drawable.bluestarnew2,50) );
        }
        newLayout.addView( makeTextView("   " + skillLevel.toString()) );
        return newLayout;
    }

    public ImageView makeImageView1(int resourceName, int widthToUse)
    {
        LinearLayout.LayoutParams layoutParams=new LinearLayout.LayoutParams(new ViewGroup.LayoutParams(widthToUse, LinearLayout.LayoutParams.WRAP_CONTENT));
        layoutParams.gravity=Gravity.CENTER;
        ImageView newImage = new ImageView(this);
        newImage.setImageResource(resourceName);
        newImage.setLayoutParams(layoutParams);

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



    public void makeProfilePicCircular()
    {
        ImageView profilePic=(ImageView)findViewById(R.id.profile_pic);

//get bitmap of the image
        Bitmap imageBitmap= BitmapFactory.decodeResource(getResources(),  R.drawable.bertcase);
        RoundedBitmapDrawable roundedBitmapDrawable= RoundedBitmapDrawableFactory.create(getResources(), imageBitmap);

//setting radius
        //roundedBitmapDrawable.setCornerRadius(50.0f);
        roundedBitmapDrawable.setCircular(true);
        roundedBitmapDrawable.setAntiAlias(true);
        profilePic.setImageDrawable(roundedBitmapDrawable);
    }
// MAHIR






    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_profile_page1);
        ll = (LinearLayout)findViewById(R.id.texts_layout);
        /////
        id = getIntent().getStringExtra("ID_FROM_LOGIN");
        name = getIntent().getStringExtra("NAME_FROM_LOGIN");
        password = getIntent().getStringExtra("PASSWORD_FROM_LOGIN");
        //secondUserId = getIntent().getStringExtra("secondUserID");

        makeProfilePicCircular();

        new ConnectionTest().execute("");


        bmImage = findViewById(R.id.profile_pic);


            new DownloadImageTask().execute("http://obsco.me/obsco/api/v1.0/" + id);

        //addUserTraits();
    }
}
