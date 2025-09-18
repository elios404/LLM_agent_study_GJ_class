package com.example.board.service;

import java.util.List;

import com.example.board.domain.BoardVO;

public interface BoardService {
    
    public List<BoardVO> getList();

    public int register(BoardVO board);

    public BoardVO get(Long bno);

    public boolean modify(BoardVO board);

    public boolean remove(Long bno);
}
