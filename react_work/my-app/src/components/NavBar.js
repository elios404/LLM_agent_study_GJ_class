import {
  Link, NavLink
} from 'react-router-dom';

const NavBar = () => {
    return (
        <nav className="navbar navbar-dark bg-dark">
            <div className="container">
            <Link className="navbar-brand" to="/">Home</Link>         
            <ul className="navbar-nav">
                <li className="nav-item">
                    {/* blogs 일때만 버튼이 흰색으로 보이도록 */}
                    <NavLink to="/blogs" end className={({isActive}) => isActive ? 'nav-link active' : 'nav-link'}>
                        Blogs
                    </NavLink>
                </li>              
            </ul>          
            </div>
        </nav>
    );
};

export default NavBar;