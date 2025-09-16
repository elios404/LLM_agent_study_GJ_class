package com.example.board.controller;

import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import com.example.board.domain.BoardVO;
import com.example.board.service.BoardService;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;



@RestController
@RequestMapping("/board/*")
public class BoardController {

    @Autowired
    BoardService service;

    // private final BoardService service;

    // public BoardController(BoardService service) {
    //     this.service = service;
    // }
    
    @GetMapping("/")
    public String hello() {
        return "Hello!";
    }

    @GetMapping("/list")
    public List<BoardVO> getList() {
        return service.getList();
    }
    
    
}
