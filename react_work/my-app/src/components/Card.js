// {children && <div>{children}</div>} 는 
// children 이 있으면 True가 되어 <div>{children}</div> 이 나올 수 있다.

const Card = ({ title, children, onClick }) => {
    return  (
        <div className="card mb-3 cursor-pointer" onClick={onClick}>
            <div className="card-body">
                <div className="d-flex justify-content-between">
                    <div>{title}</div>
                    {children && <div>{children}</div>} 
                </div>
            </div>
        </div>
    );
}

export default Card;