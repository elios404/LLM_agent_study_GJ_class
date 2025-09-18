package com.example.spring_docker;

import org.springframework.web.bind.annotation.RestController;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
// import org.springframework.web.bind.annotation.RequestParam;



@RestController
public class AppController {

    @Autowired
    MemberMapper mapper;
    
    @GetMapping("/hello")
    public String sayHello() {
        return "HI from Docker!";
    }
    
    @GetMapping("/members")
    public List<MemberVO> getAllMembers() {
        return mapper.selectAllMembers();
    }
    
}
