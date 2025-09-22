package com.example.board.domain;

import java.util.Arrays;

import lombok.Data;

@Data
public class Criteria {
    private int pageNum;
    private int amount;
    
    private String type; //title => 'T', content => 'C', writer => 'W' 
    private String keyword;

    public Criteria(){
        this(1);
    }

    public Criteria(int pageNum) {
        this.pageNum = pageNum;
        this.amount = 2;
    }

    public Criteria(int pageNum, String type, String keyword) {
        this.pageNum = pageNum;
        this.type = type;
        this.keyword = keyword;
        this.amount = 2;
    }

    public String[] getTypeArr() {
        System.out.println("############################");
        // "TCW" -> [T, C, W]
        String arr[] = (type == null ? new String[]{} : type.split(""));
        System.out.println("arr : " + Arrays.toString(arr));
        return arr;
    }
}
