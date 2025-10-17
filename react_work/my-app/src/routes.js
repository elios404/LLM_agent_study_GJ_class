import HomePage from './pages/homePage';
import CreatePage from './pages/createPage';
import EditPage from './pages/editPage';
import ListPage from './pages/listPage';

// 반복되는 내용을 배열과 map으로 처리
const routes = [
    {
        path:'/',
        element: <HomePage/>
    },
    {
        path:'/blogs',
        element: <ListPage/>
    },
    {
        path:'/blogs/create',
        element: <CreatePage/>
    },
    {
        path:'/blogs/edit',
        element: <EditPage/>
    },
]

export default routes;