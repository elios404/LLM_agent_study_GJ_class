package com.example.rest.service;

// import java.util.ArrayList;
// import java.util.Date;
// import java.util.Iterator;
import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.example.rest.domain.User;
import com.example.rest.mapper.UserMapper;

@Service // service는 비지니스 로직을 구현하는 부분
public class UserService {
    
    @Autowired
    private UserMapper mapper;

    // private static List<User> users = new ArrayList<>();
    // private static int usersCount = 3;

    // static{
    //     users.add(new User(1, "cheon", new Date()));
    //     users.add(new User(2, "se", new Date()));
    //     users.add(new User(3, "jun", new Date()));
    // }

    public List<User> findAll(){
        return mapper.findAllUsers();
    }

    public User findOne(int id){
        return mapper.findUser(id);
    }

    public User save(User user){
        mapper.createUser(user);
        return user;
    }

    // public User deleteById(int id){
    //     Iterator<User> iterator = users.iterator(); //유저 리스트를 반복하는 iterator

    //     while(iterator.hasNext()){
    //         User user = iterator.next();

    //         if(user.getId() == id){
    //             iterator.remove();
    //             return user;
    //         }
    //     }
    //     return null;
    // }
}
