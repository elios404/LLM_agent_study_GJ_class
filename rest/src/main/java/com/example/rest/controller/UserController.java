package com.example.rest.controller;

import java.net.URI;
import java.util.List;

// import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.servlet.support.ServletUriComponentsBuilder;

import com.example.rest.domain.User;
import com.example.rest.exception.UserNotFoundException;
import com.example.rest.service.UserService;

import jakarta.validation.Valid;

// import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
// import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;



@RestController
public class UserController {
    
    private UserService service;

    public UserController(UserService service){
        this.service = service;
    }


    @GetMapping("/users")
    public List<User> retrieveAllUsers() {
        return service.findAll();
    }
    

    @GetMapping("/users/{id}")
    public User retrieveUser(@PathVariable int id) {
        User user = service.findOne(id);

        if(user == null){
            throw new UserNotFoundException(String.format("ID[%s] not found", id));
        }
        
        return user;
    }


    @PostMapping("/users")
    public ResponseEntity<User> createUser(@Valid @RequestBody User user) { //클라이언트에서 오는 json을 객체로 변환 + @Valid를 통해서 유효성 체크
        User savedUser = service.save(user);
        URI location = ServletUriComponentsBuilder.fromCurrentRequest().path("/{id}").buildAndExpand(savedUser.getId()).toUri(); //현재의  uri 경로를 기반으로 새로운 uri 경로를 만들어줌.
        
        return ResponseEntity.created(location).build(); //created를 통해서 201로 상태코드 리턴
    }
    
    // @DeleteMapping("/users/{id}")
    // public User deleteUser(@PathVariable int id) {
    //     User user = service.deleteById(id);

    //     if(user == null){
    //         throw new UserNotFoundException(String.format("ID[%s] not found", id));
    //     }

    //     return user;
    // }
    
}
