
def objective ( groups , rows ) :

	return min( group - max( row[g] for row in rows ) for g , group in enumerate( groups ) )

def tableau ( R , P , affectations ) :

	groups = [ 0 for i in range( P ) ]

	rows = [ [ 0 ] * P for i in range( R ) ]

	for affectation in affectations :

		g = affectation.group
		server = affectation.server
		interval = affectation.interval
		r = interval.row

		groups[g] += server.capacity

		rows[r][g] += server.capacity

	return groups , rows


def all ( R , P , affectations ) :

	groups , rows = tableau( R , P , affectations )

	return objective( groups , rows )


def groupchange ( solution , mutation ) :

	groups = solution.groups
	rows = solution.rows

	affectation , grp = mutation

	old = affectation.group

	capacity = affectation.server.capacity

	groups[old] -= capacity
	groups[grp] += capacity

	rows[affectation.interval.row][old] -= capacity
	rows[affectation.interval.row][grp] += capacity

	obj = objective( solution.groups , solution.rows )

	groups[old] += capacity
	groups[grp] -= capacity

	rows[affectation.interval.row][old] += capacity
	rows[affectation.interval.row][grp] -= capacity

	return obj
