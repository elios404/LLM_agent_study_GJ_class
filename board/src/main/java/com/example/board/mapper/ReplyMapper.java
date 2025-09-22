package com.example.board.mapper;

import java.util.List;

import org.apache.ibatis.annotations.Mapper;

import com.example.board.domain.ReplyVO;

@Mapper
public interface ReplyMapper {
    public int insertReply(ReplyVO vo);
    public List<ReplyVO> getReplyList(Long bno);
    public ReplyVO getReply(Long rno);
    public int updateReply(ReplyVO vo);
    public int deleteReply(Long rno);
}
