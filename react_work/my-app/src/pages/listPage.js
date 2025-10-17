import axios from "axios"; // 이게 정확하게 뭐 하는거인데?
import Card from "../components/Card";
import { useState, useEffect } from "react";
import { Link } from "react-router-dom";
import { useNavigate  } from "react-router-dom";

const ListPage = () => {
    const navigate = useNavigate();
    const [posts, setPosts] = useState([]);
    const getPosts = () => {
        axios.get('http://localhost:3001/posts').then((res) => {
            setPosts(res.data);
        })
    }

    useEffect(() => {
        getPosts();
    }, []) // 의존성 배열
    
    return (
        <div>
            <div className="d-flex justify-content-between mt-1 mb-1">
                <h1>Blogs</h1>
                <div>
                    <Link to='/blogs/create' className="btn btn-success mt-1">
                        Create New
                    </Link>
                </div>
            </div>
            {
                posts.map((post) => {
                    return (
                        <Card 
                            key={post.id}
                            title={post.title}
                            onClick={() => navigate('/blogs/edit')}
                        >
                            <div>
                                <button className="btn btn-danger btn-sm" onClick={(e) => {
                                        e.stopPropagation();
                                        console.log("deleted")
                                    }}>
                                    Delete
                                </button>
                            </div>
                        </Card>
                    )
                })
            }
        </div>
    );
};

export default ListPage;