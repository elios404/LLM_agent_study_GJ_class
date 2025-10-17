import './App.css';
import {  
  Route,
  BrowserRouter as Router,
  Routes
} from 'react-router-dom';
// import BlogForm from './components/BlogForm';
import NavBar from './components/NavBar';
// NavBar BlogForm이라는 사용자 정의 태그(컴포넌트)를 만들 수 있다.
import routes from './routes';


function App() {    
  return (
    <Router>
      <NavBar/> 
      <div className='container'>
        <Routes>
          {
            // routes 배열안의 route 하나씩
            routes.map((route) => (
              <Route key={route.path} path={route.path} element={route.element} />
            ))
          }
        </Routes>
      </div>
    </Router>  
      
  );
}

export default App;
