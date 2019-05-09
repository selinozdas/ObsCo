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

import java.util.ArrayList;

public class RecyclerViewAdapterMembers extends RecyclerView.Adapter<RecyclerViewAdapterMembers.ViewHolder> {
    private static final String TAG = "RecycleViewAdapterM";

    private ArrayList<String> memberIDs;
    private ArrayList<String> memberNames;
    private String groupID;
    private String userID;
    private String password;
    private String userName;
    private Context mContext;

    public class ViewHolder extends RecyclerView.ViewHolder {

        Button memberName;
        String memberID;

        RelativeLayout parentLayout;

        public ViewHolder(@NonNull View itemView) {
            super(itemView);
            memberName = itemView.findViewById(R.id.member_name);
            parentLayout = itemView.findViewById(R.id.parent_layout);

        }
    }

    public RecyclerViewAdapterMembers (Context mContext, ArrayList<String> memberIDs, ArrayList<String> memberNames,
                                       String groupID, String userID, String userName, String password) {
        this.memberIDs = memberIDs;
        this.memberNames = memberNames;
        this.groupID = groupID;
        this.userID = userID;
        this.userName = userName;
        this.password = password;
        this.mContext = mContext;
    }

    @NonNull
    @Override
    public ViewHolder onCreateViewHolder(@NonNull ViewGroup viewGroup, int i) {
        View view = LayoutInflater.from(viewGroup.getContext()).inflate(R.layout.layout_listitem_member, viewGroup, false);
        final ViewHolder holder = new ViewHolder(view);
        holder.memberName.setOnClickListener(new View.OnClickListener()
        {
            @Override
            public void onClick(View v)
            {
                //Open new page
                Intent intent = new Intent("android.intent.action.SECONDPROFILEPAGE");
                intent.putExtra("groupID", groupID);
                intent.putExtra("ID_FROM_LOGIN", userID);
                intent.putExtra("NAME_FROM_LOGIN", userName);
                intent.putExtra("PASSWORD_FROM_LOGIN", password);
                intent.putExtra("secondUserID", holder.memberID);
                mContext.startActivity(intent);
            }
        });
        return holder;
    }

    @Override
    public void onBindViewHolder(@NonNull ViewHolder viewHolder, int position) {
        Log.d(TAG, "onBindViewHolder: called.");
        System.out.println (position);
        System.out.println (memberNames.get(position));
        System.out.println (memberNames.size());
        viewHolder.memberName.setText(memberNames.get(position));
        viewHolder.memberID = memberIDs.get(position);
    }

    @Override
    public int getItemCount() {
        return memberIDs.size();
    }


}
