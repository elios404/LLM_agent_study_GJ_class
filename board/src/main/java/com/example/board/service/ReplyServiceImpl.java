package com.example.board.service;

import java.util.List;

import org.springframework.stereotype.Service;

import com.example.board.domain.ReplyVO;
import com.example.board.mapper.ReplyMapper;

@Service
public class ReplyServiceImpl implements ReplyService {
    
    public final ReplyMapper mapper;

    public ReplyServiceImpl(ReplyMapper mapper) {
        this.mapper = mapper;
    }

    @Override
    public int insertReply(ReplyVO vo) {
        return mapper.insertReply(vo);
    }

    @Override
    public List<ReplyVO> getReplyList(Long bno) {
        return mapper.getReplyList(bno);
    }

    @Override
    public ReplyVO getReply(Long rno) {
        return mapper.getReply(rno);
    }

    @Override
    public int updateReply(ReplyVO vo) {
        return mapper.updateReply(vo);
    }

    @Override
    public int deleteReply(Long rno) {
        return mapper.deleteReply(rno);
    }
}
