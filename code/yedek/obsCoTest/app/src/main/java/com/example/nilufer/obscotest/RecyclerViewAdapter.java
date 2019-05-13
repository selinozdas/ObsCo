package com.example.nilufer.obscotest;

import android.content.Context;
import android.content.Intent;
import android.support.annotation.NonNull;
import android.support.v7.widget.RecyclerView;
import android.util.Log;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.Button;
import android.widget.RelativeLayout;
import android.widget.Toast;

import java.util.ArrayList;

public class RecyclerViewAdapter extends RecyclerView.Adapter<RecyclerViewAdapter.ViewHolder>{

    private static final String TAG = "RecycleViewAdapter";

    private ArrayList<String> groupIDs;
    private ArrayList<String> groupNames;
    private String userID;
    private String password;
    private String userName;
    private Context mContext;

    public RecyclerViewAdapter(Context mContext, ArrayList<String> groupIDs, ArrayList<String> groupNames,
                               String userID, String password, String userName) {
        this.groupIDs = groupIDs;
        this.groupNames = groupNames;
        this.userID = userID;
        this.password = password;
        this.userName = userName;
        this.mContext = mContext;
    }

    @NonNull
    @Override
    public ViewHolder onCreateViewHolder(@NonNull ViewGroup viewGroup, int i) {
        View view = LayoutInflater.from(viewGroup.getContext()).inflate(R.layout.layout_listitem, viewGroup, false);
        final ViewHolder holder = new ViewHolder(view);
        holder.groupName.setOnClickListener(new View.OnClickListener()
        {
            @Override
            public void onClick(View v)
            {

                String testString = "Member list açıldı";
                Toast.makeText(mContext, testString, Toast.LENGTH_LONG).show();

                //Open new page
                Intent intent = new Intent("android.intent.action.ML");
                intent.putExtra("groupID", holder.groupID);
                intent.putExtra("userID", userID);
                intent.putExtra("userName", userName);
                intent.putExtra("password", password);
                mContext.startActivity(intent);
            }
        });
        return holder;
    }

    @Override
    public void onBindViewHolder(@NonNull ViewHolder viewHolder, int position) {
        Log.d(TAG, "onBindViewHolder: called.");
        viewHolder.groupName.setText(groupNames.get(position));
        viewHolder.groupID = groupIDs.get(position);
        //viewHolder.groupName.setText("dummy");
    }

    @Override
    public int getItemCount() {
        return groupIDs.size();
    }

    public class ViewHolder extends RecyclerView.ViewHolder {

        //CircleImageView image;
        Button groupName;
        String groupID;

        RelativeLayout parentLayout;

        public ViewHolder(@NonNull View itemView) {
            super(itemView);
            //image = itemView.findViewById(R.id.image);
            groupName = itemView.findViewById(R.id.group_name);
            parentLayout = itemView.findViewById(R.id.parent_layout);
        }
    }
}

