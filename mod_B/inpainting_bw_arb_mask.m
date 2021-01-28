clear all
close all
clc

%HARMONIC INPAINTING FOR ARBITRARY MASK
%%%%%%%%%IMAGES
%Original image
orig_color = imread('jarnfelt_koli.png');
figure(1)
imshow(orig_color)

% % %pick one channel: %Extend this to RGB
% % % orig_chR = orig_color(:,:,1);
% % % orig_chG = orig_color(:,:,1);
% % % orig_chB = orig_color(:,:,1);
% % % figure(333)
% % % imshow(orig_1ch)

%Black and white
orig_bw = rgb2gray(orig_color);
figure(2)
imshow(orig_bw)

%Mask
mask = imread('mask.png');
figure(3)
imshow(mask)

mask_matrix = mask/255; %10268 s-points
%figure(123) 
%imshow(mask_matrix) 

%Graffiti sprayed image
%image_graf = orig_1ch .* mask_matrix; 
image_graf = orig_bw .* mask_matrix;
figure(4)
imshow(image_graf)
%%%%%%

% Create a list of j and k values (x,y coordinates) of the s-points
% to map the interior given by the arbitrary mask
s = [];
r = 0;
for j = 1:length(mask_matrix(:,1))
    for k = 1:length(mask_matrix(1,:))
        if mask_matrix(j,k) == 0
            j;,k;
            r = r + 1; %create artifical counter
            s(r,1) = j; %s(:,1) contains x coordinates
            s(r,2) = k; %s(:,2) contains y coordinates
        end
    end
end

%Discretized 2D Laplace PDE%
%Slide 22 on the slide set l1

%Ax = b with dimensions of A = (s x s) and b = (s,1)
%Initialize with speye and spzeros; but it is slow to append elements 
%to a sparse representation? this is what python says..

A = -4*eye(length(s)); %Diagonals = -(no. of nn.s for homog. PDE)
%A is symmetric also
b = zeros(length(s),1); 

for i = 1:length(s)
    j = s(i,1);
    k = s(i,2);
    for ii = 1:length(s)
        %Four terms in Laplace PDE: (j-1,k), (j+1,k), (j,k-1), (j,k+1)
        if (j-1) == s(ii,1) && k == s(ii,2)
            A(i,ii) = 1;
        else 
            b(i) = - 1*double(image_graf(j-1,k)); 
        end
        
        if (j+1) == s(ii,1) && k == s(ii,2) 
            A(i,ii) = 1;
        else
            b(i) = b(i) - 1*double(image_graf(j+1,k));
        end
        
        if j == s(ii,1) && (k-1) == s(ii,2)
            A(i,ii) = 1;
        else
            b(i) = b(i) - 1*double(image_graf(j,k-1));
        end
        
        if j == s(ii,1) && (k+1) == s(ii,2)
            A(i,ii) = 1;
        else
            b(i) =  b(i) - 1*double(image_graf(j,k+1));
        end
    end
end

%Solve Ax = b for x%
%Optimize this for sparse matrices:
%Sparse matrix if density of zeroes > 1/2 i.e., 1 - nnz(X)/(row*col) > 1/2
%Density of zeroes in A: 1 - nnz(A)/(10268^2) = 0.9996
%Density of zeroes in b: 1 - nnz(b)/(10268) = 0.8734

% %This is probably how you do it in matlab: "kenokeppi-operaatio"
% tic
x = A\b; % 6.5 s, can I reduce this by only storing sparse(A)?
% toc
% https://se.mathworks.com/help/matlab/ref/mldivide.html see bottom part for the algorithm

%Timing other methods: Running all three at same time crashes matlab
%runs out of memory?
% tic
% x = inv(A)*b; % 36 s
% toc
% 

%This symbolic crashes the program
% tic
% x = solve(A,b); %
% toc

%Restore the image: insert intensitites in x(:) to the original image

%x(i) corresponds to the intensity at a pixel given by 
%the x and y coordinates in s(i,1) and s(i,2), respectively.

%Put the value from x(i) to the position (s(i,1), s(i,2)) in the image

inpainting = double(image_graf);
for iii = 1:length(s)
    inpainting(s(iii,1),s(iii,2)) = x(iii);
end

figure(555)
imshow(uint8(inpainting))