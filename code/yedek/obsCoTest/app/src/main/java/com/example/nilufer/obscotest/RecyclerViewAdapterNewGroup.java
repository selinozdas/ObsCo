package com.example.nilufer.obscotest;

import android.content.Context;
import android.support.annotation.NonNull;
import android.support.v7.widget.RecyclerView;
import android.util.Log;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.CheckBox;
import android.widget.CompoundButton;
import android.widget.RelativeLayout;
import android.widget.TextView;

import java.util.ArrayList;

public class RecyclerViewAdapterNewGroup extends RecyclerView.Adapter<RecyclerViewAdapterNewGroup.ViewHolder> {
    private static final String TAG = "RecycleViewAdapterM";

    private ArrayList<String> eligibleNames;
    private ArrayList<String> recScores;
    private ArrayList<Boolean> checkBoxAdd;
    private ArrayList<Boolean> checkBoxLeader;
    private Context mContext;

    public class ViewHolder extends RecyclerView.ViewHolder {

        String memberID;
        TextView recScore;
        TextView memberName;
        CheckBox addMember;
        CheckBox makeLeader;

        RelativeLayout parentLayout;

        public ViewHolder(@NonNull View itemView) {
            super(itemView);
            recScore = itemView.findViewById(R.id.rec_score);
            memberName = itemView.findViewById(R.id.add_member_name);
            addMember = itemView.findViewById(R.id.add_member);
            makeLeader = itemView.findViewById(R.id.make_leader);
        }
    }

    public RecyclerViewAdapterNewGroup(Context mContext, ArrayList<String> eligibleNames, ArrayList<String> recScores,
                                       ArrayList<Boolean> checkBoxAdd, ArrayList<Boolean> checkBoxLeader) {

        this.eligibleNames =  eligibleNames;
        this.recScores = recScores;
        this.checkBoxAdd = checkBoxAdd;
        this.checkBoxLeader = checkBoxLeader;
        this.mContext = mContext;
    }

    @NonNull
    @Override
    public ViewHolder onCreateViewHolder(@NonNull ViewGroup viewGroup, int i) {
        View view = LayoutInflater.from(viewGroup.getContext()).inflate(R.layout.layout_listitem_eligible_member, viewGroup, false);
        final ViewHolder holder = new ViewHolder(view);
        return holder;
    }

    @Override
    public void onBindViewHolder(@NonNull final ViewHolder viewHolder, final int position) {
        Log.d(TAG, "onBindViewHolder: called.");
        viewHolder.memberName.setText(eligibleNames.get(position));
        viewHolder.recScore.setText(recScores.get(position));

        viewHolder.addMember.setOnCheckedChangeListener(null);
        viewHolder.makeLeader.setOnCheckedChangeListener(null);
        //if true, your checkbox will be selected, else unselected
        viewHolder.addMember.setChecked(checkBoxAdd.get(position));
        viewHolder.makeLeader.setChecked(checkBoxAdd.get(position));

        viewHolder.addMember.setOnCheckedChangeListener(new CompoundButton.OnCheckedChangeListener() {
            @Override
            public void onCheckedChanged(CompoundButton buttonView, boolean isChecked) {
                //set your object's last status
                checkBoxAdd.set(position, isChecked);
            }
        });

        viewHolder.makeLeader.setOnCheckedChangeListener(new CompoundButton.OnCheckedChangeListener() {
            @Override
            public void onCheckedChanged(CompoundButton buttonView, boolean isChecked) {
                //set your object's last status
                checkBoxLeader.set(position, isChecked);
                if ( isChecked ){
                    checkBoxAdd.set(position, true);
                    viewHolder.addMember.setChecked(true);
                }
            }
        });

    }

    @Override
    public int getItemCount() {
        return eligibleNames.size();
    }
}
