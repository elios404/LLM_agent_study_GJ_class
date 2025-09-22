package com.example.board.service;

import java.util.List;

// import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.example.board.domain.BoardVO;
import com.example.board.domain.Criteria;
import com.example.board.mapper.BoardMapper;

@Service
public class BoardServiceImpl implements BoardService {

    // 2가지 주입 방법
    // @Autowired
    // BoardMapper mapper;

    private final BoardMapper mapper;

    public BoardServiceImpl(BoardMapper mapper) {
        this.mapper = mapper;
    }

    @Override
    public List<BoardVO> getList() {
        return mapper.getList();
    }

    @Override
    public List<BoardVO> getList(int pageNum, String type, String keyword) {
        return mapper.getListWithPaging(new Criteria(pageNum, type, keyword));
    }

    @Override
    public int register(BoardVO board) {
        return mapper.insert(board);
    }

    @Override
    public BoardVO get(Long bno) {
        return mapper.read(bno);
    }

    @Override
    public boolean modify(BoardVO board) {
        return mapper.update(board) == 1;
    }

    @Override
    public boolean remove(Long bno) {
        return mapper.delete(bno) == 1;
    }
    
}
