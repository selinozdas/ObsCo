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

import java.util.ArrayList;

public class RecyclerViewAdapterSkillList extends RecyclerView.Adapter<RecyclerViewAdapterSkillList.ViewHolder> {

    private static final String TAG = "RecycleViewAdapterSL";

    private ArrayList<String> skillNames;
    private ArrayList<Boolean> checkBoxes;
    private Context mContext;

    public class ViewHolder extends RecyclerView.ViewHolder {

        CheckBox skillName;
        //Boolean checked;

        RelativeLayout parentLayout;

        public ViewHolder(@NonNull View itemView) {
            super(itemView);
            skillName = itemView.findViewById(R.id.skill_name);
            parentLayout = itemView.findViewById(R.id.parent_layout);
            //checked = false;
        }
    }

    public RecyclerViewAdapterSkillList (Context mContext, ArrayList<String> skillNames, ArrayList<Boolean> checkBoxes) {
        this.skillNames = skillNames;
        this.checkBoxes = checkBoxes;
        this.mContext = mContext;
    }

    @NonNull
    @Override
    public ViewHolder onCreateViewHolder(@NonNull ViewGroup viewGroup, int i) {
        View view = LayoutInflater.from(viewGroup.getContext()).inflate(R.layout.layout_listitem_skilllist, viewGroup, false);
        final ViewHolder holder = new ViewHolder(view);
        return holder;
    }

    @Override
    public void onBindViewHolder(@NonNull final ViewHolder viewHolder, final int position) {
        Log.d(TAG, "onBindViewHolder: called.");
        viewHolder.skillName.setText(skillNames.get(position));
        viewHolder.skillName.setOnCheckedChangeListener(null);

        //if true, your checkbox will be selected, else unselected
        viewHolder.skillName.setChecked(checkBoxes.get(position));

        viewHolder.skillName.setOnCheckedChangeListener(new CompoundButton.OnCheckedChangeListener() {
            @Override
            public void onCheckedChanged(CompoundButton buttonView, boolean isChecked) {
                //set your object's last status
                checkBoxes.set(position, isChecked);
            }
        });
    }

    @Override
    public int getItemCount() {
        return skillNames.size();
    }
}
