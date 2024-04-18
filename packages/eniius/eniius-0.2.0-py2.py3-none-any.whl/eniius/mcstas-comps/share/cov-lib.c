/*******************************************************************************
*
* McStas, neutron ray-tracing package
*         Copyright 1997-2020, All rights reserved
*         DTU Physics, Lyngby, Denmark
*         Institut Laue Langevin, Grenoble, France
*
* Library: share/cov-lib.c
*
* %Identification
* Written by: Tobias Weber <tweber@ill.fr>
* Date: Nov 20, 2020
* Origin: Institut Laue Langevin
* Release: McStas 3.0
* Version: 0.1
*
* This file is used for resolution calculations, it was taken from "tlibs2" and "matrix_calc":
*   https://code.ill.fr/scientific-software/takin/tlibs2/-/blob/master/libs/mathlib.c
*   https://github.com/t-weber/matrix_calc/blob/master/src/libs/runtime.c
*
* Usage: within SHARE
* %include "cov-lib"
*
*******************************************************************************/

#ifndef MCCODE_STRING
	#include "cov-lib.h"

	#include <math.h>
	#include <float.h>
	#include <stdlib.h>
#endif


/* ---------------------------------------------------------------------------- */
/* linked list */
/* ---------------------------------------------------------------------------- */

tl2_list_type* tl2_lst_create(void *elem)
{
	tl2_list_type* lst = (tl2_list_type*)malloc(sizeof(tl2_list_type));
	lst->elem = elem;
	lst->next = 0;

	return lst;
}


tl2_list_type* tl2_lst_append(tl2_list_type *lst, void *elem)
{
	while(lst->next)
		lst = lst->next;

	lst->next = (tl2_list_type*)malloc(sizeof(tl2_list_type));
	lst->next->elem = elem;
	lst->next->next = 0;

	return lst->next;
}


void tl2_lst_remove(tl2_list_type *lst, void *elem)
{
	tl2_list_type *lst_prev = 0;
	while(lst)
	{
		if(lst->elem == elem)
			break;
		lst_prev = lst;
		lst = lst->next;
	}

	if(lst)
	{
		/* remove element */
		if(lst->elem)
		{
			free(lst->elem);
			lst->elem = 0;
		}

		/* unlink */
		if(lst_prev)
		{
			lst_prev->next = lst->next;
			free(lst);
		}
	}
}


void tl2_lst_free(tl2_list_type *lst)
{
	if(lst && lst->next)
		tl2_lst_free(lst->next);
	if(lst && lst->elem)
		free(lst->elem);
	if(lst)
		free(lst);
}
/* ---------------------------------------------------------------------------- */



/* ---------------------------------------------------------------------------- */
/* linalg functions */
/* ---------------------------------------------------------------------------- */

static double g_tl2_eps = DBL_EPSILON;
/* #pragma acc declare create(g_tl2_eps) */


/**
 * set float epsilon
 */
void tl2_set_eps(double eps)
{
	g_tl2_eps = eps;
}


/**
 * get float epsilon
 */
double tl2_get_eps()
{
	return g_tl2_eps;
}


/**
 * tests equality of floating point numbers
 */
int tl2_flt_equals(double x, double y, double eps)
{
	double diff = x-y;
	if(diff < 0.)
		diff = -diff;
	return diff <= eps;
}


/**
 * set matrix elements to zero
 */
void tl2_mat_zero(double* M, int I, int J)
{
	for(int i=0; i<I; ++i)
		for(int j=0; j<J; ++j)
			M[i*J + j] = 0.;
}


/**
 * set vector elements to zero
 */
void tl2_vec_zero(double* vec, int N)
{
	for(int i=0; i<N; ++i)
		vec[i] = 0.;
}


/**
 * copy a vector
 */
void tl2_vec_cpy(double* dst, const double* src, int N)
{
	for(int i=0; i<N; ++i)
		dst[i] = src[i];
}


/**
 * copy a matrix
 */
void tl2_mat_cpy(double* DST, const double* SRC, int I, int J)
{
	for(int i=0; i<I; ++i)
		for(int j=0; j<J; ++j)
			DST[i*J + j] = SRC[i*J + j];
}


/**
 * removes a given row and column of a square matrix
 */
void tl2_submat(const double* M, int N, double* M_new, int iremove, int jremove)
{
	int row_new = 0;
	for(int row=0; row<N; ++row)
	{
		if(row == iremove)
			continue;

		int col_new = 0;
		for(int col=0; col<N; ++col)
		{
			if(col == jremove)
				continue;

			M_new[row_new*(N-1) + col_new] = M[row*N + col];
			++col_new;
		}
		++row_new;
	}
}


/**
 * calculates the determinant
 */
double tl2_determinant(const double* M, int N)
{
	/* special cases */
	if(N == 0)
		return 0;
	else if(N == 1)
		return M[0];
	else if(N == 2)
		return M[0*N+0]*M[1*N+1] - M[0*N+1]*M[1*N+0];


	/* get row with maximum number of zeros */
	int row = 0;
	int maxNumZeros = 0;
	for(int curRow=0; curRow<N; ++curRow)
	{
		int numZeros = 0;
		for(int curCol=0; curCol<N; ++curCol)
		{
			if(tl2_flt_equals(M[curRow*N + curCol], 0, g_tl2_eps))
				++numZeros;
		}

		if(numZeros > maxNumZeros)
		{
			row = curRow;
			maxNumZeros = numZeros;
		}
	}


	/* recursively expand determiant along a row */
	double fullDet = 0.;

	double *submat = (double*)malloc((N-1)*(N-1) * sizeof(double));
	for(int col=0; col<N; ++col)
	{
		const double elem = M[row*N + col];
		if(tl2_flt_equals(elem, 0, g_tl2_eps))
			continue;

		tl2_submat(M, N, submat, row, col);
		const double sgn = ((row+col) % 2) == 0 ? 1. : -1.;
		fullDet += elem * tl2_determinant(submat, N-1) * sgn;
	}
	free(submat);

	return fullDet;
}


/**
 * inverted matrix
 */
int tl2_inverse(const double* M, double* I, int N)
{
	double fullDet = tl2_determinant(M, N);

	/* fail if determinant is zero */
	if(tl2_flt_equals(fullDet, 0., g_tl2_eps))
		return 0;

	double *submat = (double*)malloc((N-1)*(N-1) * sizeof(double));
	for(int i=0; i<N; ++i)
	{
		for(int j=0; j<N; ++j)
		{
			tl2_submat(M, N, submat, i, j);
			const double sgn = ((i+j) % 2) == 0 ? 1. : -1.;
			I[j*N + i] = tl2_determinant(submat, N-1) * sgn / fullDet;
		}
	}
	free(submat);

	return 1;
}


/**
 * matrix-matrix product
 */
void tl2_matmat_mul(const double* M1, const double* M2, double *RES, int I, int J, int K)
{
	for(int i=0; i<I; ++i)
	{
		for(int j=0; j<J; ++j)
		{
			RES[i*J + j] = 0.;

			for(int k=0; k<K; ++k)
				RES[i*J + j] += M1[i*K + k]*M2[k*J + j];
		}
	}
}


/**
 * matrix-vector product
 */
void tl2_matvec_mul(const double* M, const double* v, double *res, int I, int J)
{
	for(int i=0; i<I; ++i)
	{
		res[i] = 0.;
		for(int j=0; j<J; ++j)
		{
			res[i] += M[i*J + j]*v[j];
		}
	}
}


/**
 * transposed matrix
 */
void tl2_transpose(const double* M, double* T, int rows, int cols)
{
	for(int ctr=0; ctr<rows*cols; ++ctr)
	{
		int i = ctr/cols;
		int j = ctr%cols;
		T[j*rows + i] = M[i*cols + j];
	}
}


/**
 * vector inner product
 */
double tl2_inner(const double* v0, const double* v1, int N)
{
	double res = 0.;
	for(int i=0; i<N; ++i)
		res += v0[i]*v1[i];
	return res;
}


/**
 * vector outer product
 */
void tl2_outer(const double* v0, const double* v1, double *M, int N)
{
	for(int i=0; i<N; ++i)
		for(int j=0; j<N; ++j)
			M[i*N + j] = v0[i] * v1[j];
}


/**
 * 3-vector cross product
 */
void tl2_cross(const double* v0, const double* v1, double *res)
{
	res[0] = v0[1]*v1[2] - v0[2]*v1[1];
	res[1] = v0[2]*v1[0] - v0[0]*v1[2];
	res[2] = v0[0]*v1[1] - v0[1]*v1[0];
}


/**
 * vector length
 */
double tl2_vec_len(const double* vec, int N)
{
	double len = tl2_inner(vec, vec, N);
	return sqrt(len);
}


/**
 * vector addition
 */
void tl2_vec_add(const double* v0, const double* v1, double *res, int N)
{
	for(int i=0; i<N; ++i)
		res[i] = v0[i] + v1[i];
}


/**
 * vector subtraction
 */
void tl2_vec_sub(const double* v0, const double* v1, double *res, int N)
{
	for(int i=0; i<N; ++i)
		res[i] = v0[i] - v1[i];
}


/**
 * negative vector
 */
void tl2_vec_neg(const double* vec, double *res, int N)
{
	for(int i=0; i<N; ++i)
		res[i] = -vec[i];
}


/**
 * vector-scalar multiplication
 */
void tl2_vec_mul(const double* vec, double s, double *res, int N)
{
	for(int i=0; i<N; ++i)
		res[i] = vec[i] * s;
}


/**
 * vector-scalar division
 */
void tl2_vec_div(const double* vec, double s, double *res, int N)
{
	tl2_vec_mul(vec, 1./s, res, N);
}


/**
 * matrix addition
 */
void tl2_mat_add(const double* M0, const double* M1, double *RES, int I, int J)
{
	for(int i=0; i<I; ++i)
		for(int j=0; j<J; ++j)
			RES[i*J + j] = M0[i*J + j] + M1[i*J + j];
}


/**
 * matrix subtraction
 */
void tl2_mat_sub(const double* M0, const double* M1, double *RES, int I, int J)
{
	for(int i=0; i<I; ++i)
		for(int j=0; j<J; ++j)
			RES[i*J + j] = M0[i*J + j] - M1[i*J + j];
}


/**
 * negative matrix
 */
void tl2_mat_neg(const double* M, double *RES, int I, int J)
{
	for(int i=0; i<I; ++i)
		for(int j=0; j<J; ++j)
			RES[i*J + j] = - M[i*J + j];
}


/**
 * matrix-scalar multiplication
 */
void tl2_mat_mul(const double* M, double s, double *RES, int I, int J)
{
	for(int i=0; i<I; ++i)
		for(int j=0; j<J; ++j)
			RES[i*J + j] = M[i*J + j] * s;
}


/**
 * matrix-scalar division
 */
void tl2_mat_div(const double* M, double s, double *RES, int I, int J)
{
	tl2_mat_mul(M, 1./s, RES, I, J);
}


/**
 * mean vector
 */
void tl2_vec_mean(const tl2_list_type* veclist, const tl2_list_type* problist,
	double* mean, int N)
{
	tl2_vec_zero(mean, N);
	double prob = 0.;
	double *vec = (double*)malloc(N * sizeof(double));

	while(veclist)
	{
		tl2_vec_cpy(vec, (double*)veclist->elem, N);
		double p = 1.;

		if(problist)
		{
			p = *(double*)problist->elem;
			tl2_vec_mul(vec, p, vec, N);
		}

		tl2_vec_add(mean, vec, mean, N);
		prob += p;

		veclist = veclist->next;
		if(problist) problist = problist->next;
	}

	tl2_vec_div(mean, prob, mean, N);

	free(vec);
}


/**
 * covariance matrix
 */
int tl2_covariance(const tl2_list_type* veclist, const tl2_list_type* problist,
	double* COV, double* mean, int N)
{
	tl2_mat_zero(COV, N, N);
	tl2_vec_mean(veclist, problist, mean, N);

	double *vec = (double*)malloc(N * sizeof(double));
	double *dev = (double*)malloc(N * sizeof(double));
	double *outer = (double*)malloc(N*N * sizeof(double));
	double prob = 0.;
	unsigned int num_events = 0;

	while(veclist)
	{
		tl2_vec_cpy(vec, (double*)veclist->elem, N);
		double p = 1.;

		tl2_vec_sub(vec, mean, dev, N);
		tl2_outer(dev, dev, outer, N);

		if(problist)
		{
			p = *(double*)problist->elem;
			tl2_mat_mul(outer, p, outer, N, N);
		}

		tl2_mat_add(COV, outer, COV, N, N);
		prob += p;

		veclist = veclist->next;
		if(problist) problist = problist->next;
		++num_events;
	}

	tl2_mat_div(COV, prob, COV, N, N);

	free(vec);
	free(dev);
	free(outer);

	return num_events > 0;
}


/**
 * matrix trafo
 */
void tl2_mat_trafo(const double* M, const double* T, double* RES, int N, int ortho)
{
	double *Tinv = (double*)malloc(N*N * sizeof(double));
	double *TMP = (double*)malloc(N*N * sizeof(double));

	if(ortho)
		tl2_transpose(T, Tinv, N, N);
	else
		tl2_inverse(T, Tinv, N);

	tl2_matmat_mul(Tinv, M, TMP, N, N, N);
	tl2_matmat_mul(TMP, T, RES, N, N, N);

	free(Tinv);
	free(TMP);
}


/**
 * resolution matrix
 */
int tl2_reso(const tl2_list_type* veclist, const tl2_list_type* problist,
	double* COV, double* RESO)
{
	const int N = 4;
	tl2_mat_zero(COV, N, N);
	tl2_mat_zero(RESO, N, N);

	double *Qmean = (double*)malloc(N * sizeof(double));
	if(!tl2_covariance(veclist, problist, COV, Qmean, N))
	{
		free(Qmean);
		return 0;
	}

	double *Qdir = (double*)malloc(N * sizeof(double));
	double Qlen = tl2_vec_len(Qmean, N-1);
	tl2_vec_div(Qmean, Qlen, Qdir, N-1);

	double *Qup = (double*)malloc(N * sizeof(double));
	tl2_vec_zero(Qup, N);
	Qup[1] = 1;

	double *Qside = (double*)malloc(N * sizeof(double));
	tl2_vec_zero(Qside, N);
	tl2_cross(Qup, Qdir, Qside);

	double *T = (double*)malloc(N*N * sizeof(double));
	tl2_mat_zero(T, N, N);
	for(int i=0; i<N; ++i)
	{
		T[i*N + 0] = Qdir[i];
		T[i*N + 1] = Qside[i];
		T[i*N + 2] = Qup[i];
	}
	T[3*N + 3] = 1;

	tl2_mat_trafo(COV, T, COV, N, 1);
	tl2_inverse(COV, RESO, N);

	free(Qside);
	free(Qup);
	free(T);
	free(Qdir);
	free(Qmean);

	return 1;
}
/* ---------------------------------------------------------------------------- */



/* ----------------------------------------------------------------------------- */
/* Helper functions */
/* ----------------------------------------------------------------------------- */
double tl2_k_to_E(double kix, double kiy, double kiz, double kfx, double kfy, double kfz)
{
	const double k2_to_E = 2.0721247;  /* from codata values*/
	return k2_to_E * (kix*kix + kiy*kiy + kiz*kiz - kfx*kfx - kfy*kfy - kfz*kfz);
}
/* ----------------------------------------------------------------------------- */
