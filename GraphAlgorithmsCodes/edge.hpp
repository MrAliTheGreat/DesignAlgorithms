class Edge
{
public:
    int u,v,w,ind;
    Edge(int _u, int _v,int _w,int _ind=0) : u(_u), v(_v), w(_w), ind(_ind) { }
    
    bool operator<(Edge other)
    {
        return this->w < other.w;
    }
};