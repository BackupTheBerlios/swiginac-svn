
class ex;
class archive_node;

template <template <class> class C> class container;

/** To distinguish between different kinds of non-commutative objects */
struct return_type_t;

template<typename T> inline return_type_t make_return_type_t(const unsigned rl = 0);

/** This class stores information about a registered GiNaC class. */
class registered_class_options {
public:
    registered_class_options(const char *n, const char *p, 
                            const std::type_info& ti);

    const char *get_name() const { return name; }
    const char *get_parent_name() const { return parent_name; }
    std::type_info const* get_id() const { return tinfo_key; }
    const std::vector<print_functor> &get_print_dispatch_table() const { return print_dispatch_table; }

    template <class Ctx, class T, class C>
    registered_class_options & print_func(void f(const T &, const C & c, unsigned));

    template <class Ctx, class T, class C>
    registered_class_options & print_func(void (T::*f)(const C &, unsigned));

    template <class Ctx>
    registered_class_options & print_func(const print_functor & f);

    void set_print_func(unsigned id, const print_functor & f);

};

typedef class_info<registered_class_options> registered_class_info;

