package com.example.board.service;

import java.util.List;

import com.example.board.domain.ReplyVO;

public interface ReplyService {
        public int insertReply(ReplyVO vo);
    public List<ReplyVO> getReplyList(Long bno);
    public ReplyVO getReply(Long rno);
    public int updateReply(ReplyVO vo);
    public int deleteReply(Long rno);
}
