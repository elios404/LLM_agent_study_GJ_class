package com.example.rest.controller;

import org.springframework.web.bind.annotation.RestController;

import com.example.rest.domain.HelloWorldBean;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestParam;


@RestController // 객체만 리턴해도 responseBody 이용해서 json으로 만들어서 리턴해줌?
public class HelloController {
    
    @GetMapping("/hello")
    public String hello() {

        return "Hello Spring";
    }
    
    @GetMapping("/hello-bean")
    public HelloWorldBean helloBean() {

        return new HelloWorldBean("hello World Bean!!"); // RestController 이기에 객체로 리턴해도 자동으로 json으로 보냄
    }

    @GetMapping("/hello-bean/path-variable/{name}/{age}") // {} 를 통해서 데이터를 전달할 수 있다.
    public HelloWorldBean helloBeanName(@PathVariable String name, @PathVariable int age) {
        return new HelloWorldBean(String.format("Hello world Bean, %s, %d", name, age));
    }
    
}
