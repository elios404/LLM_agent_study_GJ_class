package com.example.board.mapper;

import java.util.List;

import org.apache.ibatis.annotations.Mapper;

import com.example.board.domain.BoardVO;

@Mapper
public interface BoardMapper {
    
    public List<BoardVO> getList();

    public int insert(BoardVO vo);

    public BoardVO read(Long bno);

    public int update(BoardVO board);

    public int delete(Long bno);
}
