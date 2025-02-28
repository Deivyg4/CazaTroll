PGDMP      8                }         	   CazaTroll    16.6    16.6                0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false                       0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false                       0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false                       1262    16397 	   CazaTroll    DATABASE     �   CREATE DATABASE "CazaTroll" WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'Spanish_Venezuela.1252';
    DROP DATABASE "CazaTroll";
                postgres    false            �            1259    40990 	   productos    TABLE     �   CREATE TABLE public.productos (
    id integer NOT NULL,
    nombre character varying(255) NOT NULL,
    precio numeric(10,2) NOT NULL,
    cantidad integer NOT NULL
);
    DROP TABLE public.productos;
       public         heap    postgres    false            �            1259    40989    productos_id_seq    SEQUENCE     �   CREATE SEQUENCE public.productos_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 '   DROP SEQUENCE public.productos_id_seq;
       public          postgres    false    220                       0    0    productos_id_seq    SEQUENCE OWNED BY     E   ALTER SEQUENCE public.productos_id_seq OWNED BY public.productos.id;
          public          postgres    false    219            �            1259    32782    roles    TABLE     `   CREATE TABLE public.roles (
    id integer NOT NULL,
    name character varying(50) NOT NULL
);
    DROP TABLE public.roles;
       public         heap    postgres    false            �            1259    32781    roles_id_seq    SEQUENCE     �   CREATE SEQUENCE public.roles_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 #   DROP SEQUENCE public.roles_id_seq;
       public          postgres    false    218                       0    0    roles_id_seq    SEQUENCE OWNED BY     =   ALTER SEQUENCE public.roles_id_seq OWNED BY public.roles.id;
          public          postgres    false    217            �            1259    24590    users    TABLE     S  CREATE TABLE public.users (
    id integer NOT NULL,
    username character varying(50) NOT NULL,
    email character varying(100) NOT NULL,
    password_hash character varying(255) NOT NULL,
    created_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    last_login timestamp without time zone,
    role_id integer DEFAULT 1
);
    DROP TABLE public.users;
       public         heap    postgres    false            �            1259    24589    users_id_seq    SEQUENCE     �   CREATE SEQUENCE public.users_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 #   DROP SEQUENCE public.users_id_seq;
       public          postgres    false    216                       0    0    users_id_seq    SEQUENCE OWNED BY     =   ALTER SEQUENCE public.users_id_seq OWNED BY public.users.id;
          public          postgres    false    215            ^           2604    40993    productos id    DEFAULT     l   ALTER TABLE ONLY public.productos ALTER COLUMN id SET DEFAULT nextval('public.productos_id_seq'::regclass);
 ;   ALTER TABLE public.productos ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    220    219    220            ]           2604    32785    roles id    DEFAULT     d   ALTER TABLE ONLY public.roles ALTER COLUMN id SET DEFAULT nextval('public.roles_id_seq'::regclass);
 7   ALTER TABLE public.roles ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    217    218    218            Z           2604    24593    users id    DEFAULT     d   ALTER TABLE ONLY public.users ALTER COLUMN id SET DEFAULT nextval('public.users_id_seq'::regclass);
 7   ALTER TABLE public.users ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    215    216    216            �          0    40990 	   productos 
   TABLE DATA           A   COPY public.productos (id, nombre, precio, cantidad) FROM stdin;
    public          postgres    false    220   3       �          0    32782    roles 
   TABLE DATA           )   COPY public.roles (id, name) FROM stdin;
    public          postgres    false    218   �       �          0    24590    users 
   TABLE DATA           d   COPY public.users (id, username, email, password_hash, created_at, last_login, role_id) FROM stdin;
    public          postgres    false    216   �       	           0    0    productos_id_seq    SEQUENCE SET     >   SELECT pg_catalog.setval('public.productos_id_seq', 9, true);
          public          postgres    false    219            
           0    0    roles_id_seq    SEQUENCE SET     :   SELECT pg_catalog.setval('public.roles_id_seq', 2, true);
          public          postgres    false    217                       0    0    users_id_seq    SEQUENCE SET     ;   SELECT pg_catalog.setval('public.users_id_seq', 24, true);
          public          postgres    false    215            j           2606    40995    productos productos_pkey 
   CONSTRAINT     V   ALTER TABLE ONLY public.productos
    ADD CONSTRAINT productos_pkey PRIMARY KEY (id);
 B   ALTER TABLE ONLY public.productos DROP CONSTRAINT productos_pkey;
       public            postgres    false    220            f           2606    32789    roles roles_name_key 
   CONSTRAINT     O   ALTER TABLE ONLY public.roles
    ADD CONSTRAINT roles_name_key UNIQUE (name);
 >   ALTER TABLE ONLY public.roles DROP CONSTRAINT roles_name_key;
       public            postgres    false    218            h           2606    32787    roles roles_pkey 
   CONSTRAINT     N   ALTER TABLE ONLY public.roles
    ADD CONSTRAINT roles_pkey PRIMARY KEY (id);
 :   ALTER TABLE ONLY public.roles DROP CONSTRAINT roles_pkey;
       public            postgres    false    218            `           2606    24600    users users_email_key 
   CONSTRAINT     Q   ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_email_key UNIQUE (email);
 ?   ALTER TABLE ONLY public.users DROP CONSTRAINT users_email_key;
       public            postgres    false    216            b           2606    24596    users users_pkey 
   CONSTRAINT     N   ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_pkey PRIMARY KEY (id);
 :   ALTER TABLE ONLY public.users DROP CONSTRAINT users_pkey;
       public            postgres    false    216            d           2606    24598    users users_username_key 
   CONSTRAINT     W   ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_username_key UNIQUE (username);
 B   ALTER TABLE ONLY public.users DROP CONSTRAINT users_username_key;
       public            postgres    false    216            �   �   x�-�9�0E�?��4^�����B4#d	$��m(�%��� ��=��c�7���I'6��F�^Ҍ'��>�k̰~1=	�S���c�S���k��EaZ!��������@=v�5+��c1��m�-:"� ��&�      �      x�3�LL����2�,-N-����� : �      �   �  x�eUˎ7<�~��B?�n��!��M20��"����6@��
��@�f��#v}���������Vo���9����6���T�W�����+���������{Q�T������E�G����M
�(m�~ܓ֚9W���3���J�U�λ����;��Н�qc�Ay��5��?�9?1��r�h��hp���O�Z���b��=@�[��s�4���l,Mc�&9�ƔvƜ��D*p
m��s�r<�Z�6�/��r7���e�b���Vk�z��u������qFZ��kDh7kcM>G��XM��)�鱝�صf����|�R�d46�L
8�\$��U�S�O[V���/��.vi��yڨy�wm��>�'>�1��\8���Σ#�%�v��dxk;kp7_��w��ܜ}��#py�gV��6�{�vypuf�r0�&���;t�u����-(�5���^�~����%�sQ;�����&`�9&����"�xs/�ƛ��������amk���8��ku+:P?h�*x���}(7?�F@��)0��[�CJ��i|���x�҄�=�Pa�Vf���ԩ},gߋK�Q]�@j�fk��2Bbu���-:�9}�a ^�ڮ��)c_z0³L�EtG�=o&ɏ�?y��$w行d��~\?��_5�5� �B,TQ�du-B���]�g�X%b�ʱZ<d��b=;����ggc��f���	�nG�d��f��r����C�Gj���ǳ*vj��*$�RSj<�4�'�y��0n��%B��ʒ��H�N���I�mf�dig��ٓ��т��:`A�l���K�Q�w��;�P��w�`�����3�c���%������QVJ�W���YD���>2�8���D��@�<���#�����MV`pp�-A(�y��h����55���������*�T}Fȑe��~{yy�p�x     