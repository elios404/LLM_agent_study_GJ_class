package com.example.board.controller;

import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import com.example.board.domain.ReplyVO;
import com.example.board.service.ReplyService;

import java.util.List;

import org.apache.catalina.connector.Response;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.PutMapping;




@RestController
@RequestMapping("/replies/*")
public class ReplyController {

    private ReplyService service;

    public ReplyController(ReplyService service) {
        this.service = service;
    }

    @PostMapping("/new")
    public ResponseEntity<String> create(@RequestBody ReplyVO vo) {
        //success, HTTP 200
        int result = service.insertReply(vo);

        return new ResponseEntity<String>(result == 1 ? "삽입 성공" : "삽입 실패", HttpStatus.OK);
    }

    @GetMapping("/list/{bno}")
    public ResponseEntity<List<ReplyVO>> getList(@PathVariable Long bno) {
        
        return new ResponseEntity<List<ReplyVO>>(service.getReplyList(bno), HttpStatus.OK);
    }

    @GetMapping("/{rno}")
    public ResponseEntity<ReplyVO> getReply(@PathVariable Long rno) {
        
        return new ResponseEntity<ReplyVO>(service.getReply(rno), HttpStatus.OK);
    }

    @PutMapping("/{rno}")
    public ResponseEntity<String> modify(@PathVariable Long rno, @RequestBody ReplyVO vo) {
        vo.setRno(rno);
        
        int result = service.updateReply(vo);

        return new ResponseEntity<String>(result == 1 ? "갱신 성공" : "갱신 실패", HttpStatus.OK);
    }
    
    @DeleteMapping("/{rno}")
    public ResponseEntity<String> remove(@PathVariable Long rno) {

        return new ResponseEntity<String>(service.deleteReply(rno) == 1 ? "삭제 성공" : "삭제 실패", HttpStatus.OK);
    }
    
}
