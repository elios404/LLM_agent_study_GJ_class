package com.example.rest.domain;

import java.util.Date;
import java.util.List;

import jakarta.validation.constraints.Past;
import jakarta.validation.constraints.Size;
import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

@Data
@AllArgsConstructor
@NoArgsConstructor
public class User {
    private Integer id;
    @Size(min = 2, message = "Name should be at least 2 charaters")
    private String name;
    @Past(message = "joinDate can't be in the past")
    private Date joinDate;
    private List<Post> posts;
}
