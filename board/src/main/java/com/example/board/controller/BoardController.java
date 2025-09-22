package com.example.board.controller;

import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import com.example.board.domain.BoardVO;
import com.example.board.service.BoardService;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.RequestBody;


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

    // @GetMapping("/list/{pageNum}")
    // public ResponseEntity<List<BoardVO>> listPaging(@PathVariable int pageNum) {
    //     return new ResponseEntity<List<BoardVO>>(service.getList(pageNum), HttpStatus.OK);
    // }

    @GetMapping("/list/{pageNum}/{type}/{keyword}")
    public ResponseEntity<List<BoardVO>> listPagingSearch(@PathVariable int pageNum, @PathVariable String type, @PathVariable String keyword) {
        return new ResponseEntity<List<BoardVO>>(service.getList(pageNum, type, keyword), HttpStatus.OK);
    }
    

    @GetMapping("/list")
    public ResponseEntity<List<BoardVO>> getList() {
        return new ResponseEntity<List<BoardVO>>(service.getList(), HttpStatus.OK);
    }

    @PostMapping("/register")
    public ResponseEntity<String> register(@RequestBody BoardVO board) {
        int insertCount = service.register(board);

        return insertCount == 1 ? new ResponseEntity<String>("success", HttpStatus.OK) : new ResponseEntity<String>(HttpStatus.INTERNAL_SERVER_ERROR);
    }

    @GetMapping("get/{bno}")
    public ResponseEntity<BoardVO> getBoard(@PathVariable Long bno) {
        return new ResponseEntity<BoardVO>(service.get(bno), HttpStatus.OK);
    }
    
    @PutMapping("/modify/{bno}")
    public ResponseEntity<String> modify(@PathVariable Long bno, @RequestBody BoardVO board) {
        board.setBno(bno);

        return service.modify(board) ? new ResponseEntity<String>("success", HttpStatus.OK) : new ResponseEntity<String>(HttpStatus.INTERNAL_SERVER_ERROR);
    }

    @DeleteMapping("/remove/{bno}")
    public ResponseEntity<String> remove(@PathVariable Long bno) {
        return service.remove(bno) ? new ResponseEntity<String>("success", HttpStatus.OK) : new ResponseEntity<String>(HttpStatus.INTERNAL_SERVER_ERROR);
    }
    
    
    
}
