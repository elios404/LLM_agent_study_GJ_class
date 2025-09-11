package com.example.rest.mapper;

import java.util.List;

import org.apache.ibatis.annotations.Mapper;

import com.example.rest.domain.User;

@Mapper
public interface UserMapper {
    public List<User> findAllUsers();
    public User findUser(int id);
    public void createUser(User user);
}
